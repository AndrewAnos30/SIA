from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import Stocks, STOCK_CATEGORY, STOCK_QUANTITY
from .models import MenuCategory, MenuDrinks, TYPES_MENU, total_AO, buyItem
from pos import views
from .forms import IngridientsForm, AddOnsForm, UtensilsForm
from .forms import MenuCategoryForm, MenuDrinksForm, BuyItemForms
import logging
import random
from datetime import datetime, timedelta
from django.db.models import Sum
from django.db.models.functions import Coalesce, Cast
from django.db.models import FloatField, IntegerField
from django.db.models.expressions import Value
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from operator import attrgetter
from django.db.models import Max
from django.db import models
from django.db.models import F, Sum


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed auth_login function
            if user.username == 'user1':
                return redirect('pos:index')
            elif user.username == 'user2':
                return redirect('pos:cashier')
            elif user.username == 'user3':
                return redirect('pos:home')
        else:
            return redirect('pos:login')
    else:
        return render(request, 'login.html')
        
@login_required
def index(request):
    today = datetime.today()

    total_all_payment = buyItem.objects.filter(dateordered__date=today).aggregate(
        total=Coalesce(Sum(Cast('AllPayment', output_field=FloatField())), Value(0), output_field=FloatField())
    )['total']
    buyitem = buyItem.objects.filter(dateordered__date=today)
    total_buy_names = buyItem.objects.filter(dateordered__date=today).values('buyName').distinct().count()
    menuDrinks = MenuDrinks.objects.all()
    menucategory = MenuCategory.objects.all()
    
    context = {
        'total_all_payment': total_all_payment,
        'buyitem': buyitem,
        'total_buy_names': total_buy_names,
        'menuDrinks': menuDrinks,
        'menucategory': menucategory
    }
    return render(request, 'index.html', context)

#inventory start
@login_required
def inventory(request):
    ingridientForm = IngridientsForm()
    my_data_ingredients = Stocks.objects.all()
    my_data_addOns = Stocks.objects.all()
    my_data_utensils = Stocks.objects.all()
    all_stocks = my_data_ingredients.union(my_data_addOns, my_data_utensils)
    addOnsForm = AddOnsForm()
    utensilsForm = UtensilsForm()

    context = {
        "stock_category": STOCK_CATEGORY,
        "stock_quantity": STOCK_QUANTITY,
        "my_data_i" : my_data_ingredients.filter(stockcategory="INGR"),
        "my_data_a" : my_data_addOns.filter(stockcategory="AO"),
        "my_data_u" : my_data_utensils.filter(stockcategory="UTNSL"),
        "all_stocks": all_stocks,
        "ingridientForm": ingridientForm,
        "addOnsForm" : addOnsForm,
        "utensilsForm" : utensilsForm,
    }

    return render(request, "inventory.html", context)

def addIngridients(request):
    if request.method == "POST":
        form = IngridientsForm(data=request.POST)
       
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse("pos:inventory"))

def addAddOns(request):
    if request.method == "POST":
        form = AddOnsForm(data=request.POST)

        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse("pos:inventory"))

def addUtensils(request):
    
    if request.method == "POST":
        form = UtensilsForm(data=request.POST)

        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse("pos:inventory"))


def update_stock(request):
    if request.method == 'POST':
        stock_id = request.POST.get('stockname')
        new_stockname = request.POST.get('new_stockname')
        stockcategory = request.POST.get('stockcategory')
        stockquantity = request.POST.get('stockquantity')
        stockmeasurement = request.POST.get('stockmeasurement')
        stockdate_in = request.POST.get('stockdate_in')
        stockexpiration = request.POST.get('stockexpiration')

        stock = get_object_or_404(Stocks, id=stock_id)
        stock.stockname = new_stockname
        stock.stockcategory = stockcategory
        stock.stockquantity = stockquantity
        stock.stockmeasurement = stockmeasurement
        stock.stockdate_in = stockdate_in
        stock.stockexpiration = stockexpiration
        stock.save()

        return redirect('pos:inventory')  # Redirect to the inventory page or any other appropriate URL

    return render(request, 'update_stock.html')

def delete_stock(request):
    if request.method == 'POST':
        stock_id = request.POST.get('stock_id')
        stock = get_object_or_404(Stocks, id=stock_id)
        stock.delete()
        return redirect('pos:inventory')  # Replace with the appropriate URL

    return render(request, 'delete_stock.html')

#inventory end
@login_required
def menu(request):
    menucategoryform = MenuCategoryForm   
    menudrinksform = MenuDrinksForm
    stocks = Stocks.objects.all()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory= MenuCategory.objects.all()

    
    context ={
    "menucategoryform" : menucategoryform,
    "menudrinksform" : menudrinksform,
    "stocks" : stocks,
    "menuDrinks" : menuDrinks,
    "menuCategory" : menuCategory,

    }
    return render(request, 'menu.html', context)

def addMenuCategory(request):
    if request.method == "POST":
        form = MenuCategoryForm(data=request.POST)
       
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse("pos:menu"))



def edit_menu_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        new_category_type = request.POST.get('categorytype')
        new_name = request.POST.get('new_name')

        category = get_object_or_404(MenuCategory, id=category_id)
        category.categorytype = new_category_type
        category.name = new_name
        category.save()

        # Redirect or render a success message

    return redirect('pos:menu')  # Replace with your appropriate redirect URL




def addMenuDrinks(request):
    if request.method == "POST":
        form = MenuDrinksForm(request.POST, request.FILES)
        
        if form.is_valid():
            if form.cleaned_data['menuimage']:
                form.save()
                logging.info("MenuDrinks object saved to database: %s", form.cleaned_data)
            else:
                logging.error("MenuDrinks form is invalid: menuimage field is required")
        else:
            logging.error("MenuDrinks form is invalid: %s", form.errors)
    else:
        logging.warning("addMenuDrinks function called with HTTP GET request")

    return HttpResponseRedirect(reverse("pos:menu"))

def delete_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        try:
            category = MenuCategory.objects.get(id=category_id)
            category.delete()
            return redirect('pos:menu')  # Replace 'pos:categories' with the actual URL name for your categories page
        except MenuCategory.DoesNotExist:
            # Handle case when category is not found
            pass
    return render(request, 'menu.html')  

def delete_menu(request, menu_id):
    try:
        menu = MenuDrinks.objects.get(id=menu_id)
        menu.delete()
        messages.success(request, 'Menu item deleted successfully.')
    except MenuDrinks.DoesNotExist:
        messages.error(request, 'Menu item not found.')
    
    return redirect(reverse('pos:menu'))
#MENU END

#HOME START
@login_required
def home(request):
    buyitemform = BuyItemForms()  # Instantiate the form
    stocks = Stocks.objects.first()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory = MenuCategory.objects.all()
    buyitem = buyItem.objects.all()

    context = {
        'buyitemform': buyitemform,
        'stocks': stocks,
        'menuDrinks': menuDrinks,
        'menuCategory': menuCategory,
        'buyitem': buyitem,
    }
    return render(request, 'home.html', context)


def buy_item_drinks(request):
    if request.method == 'POST':
        form = BuyItemForms(request.POST, request.FILES)
        if form.is_valid():
         
            form.save()
            return HttpResponseRedirect(reverse("pos:home"))
        else:
            print(form.errors)  # Check for any form errors in the console

    return HttpResponseRedirect(reverse("pos:home"))

def buy_item_drinks1(request):
    if request.method == 'POST':
        form = BuyItemForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pos:home"))
        else:
            print(form.errors)  # Check for any form errors in the console

    return HttpResponseRedirect(reverse("pos:reco"))


def update_values(request):
    if request.method == 'POST':
        # Get the form data from the request
        payment_method = request.POST.get('payment_method')
        dine_in_out = request.POST.get('DineIn_Out')
        pwd_discount = request.POST.get('PWD_discount')
        pwd_id = request.POST.get('PWD_Id', '')  # Optional, set a default value
        AllPayment = float(request.POST.get('AllPayment'))

        # Generate a unique order number
        order_number = str(random.randint(1, 99999)).zfill(5)

        # Get only the buyItem objects with transaction=False
        buy_items = buyItem.objects.filter(transaction=False)


        # Update other fields for each buyItem object
        for item in buy_items:
            if not item.transaction:
                item.payment_method = payment_method
                item.DineIn_Out = dine_in_out
                item.PWD_discount = pwd_discount
                item.PWD_Id = pwd_id
                item.orderNumber = order_number
                item.AllPayment = AllPayment
                item.transaction = True
                item.save()

        # Render the success page with the order number
        context = {'order_number': order_number}
        return render(request, 'success.html', context)

    # Render the form
    return render(request, 'cart.html')
#home end

@login_required
def sales(request):
   
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Get the start date of the current week
    end_of_week = start_of_week + timedelta(days=6)  # Get the end date of the current week
    buyitem = buyItem.objects.filter(dateordered__date__range=[start_of_week, end_of_week])
    
    context = {
        'buyitem': buyitem,
    }
    
    return render(request, 'sales.html', context)

@login_required
def order(request):
    buyitemform = BuyItemForms() 
    stocks = Stocks.objects.first()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory = MenuCategory.objects.all()
    buyitem = buyItem.objects.all()
    total_price = calculate_total_price(buyitem)
    

    context = {
        'buyitemform': buyitemform,
        'stocks': stocks,
        'menuDrinks': menuDrinks,
        'menuCategory': menuCategory,
        'buyitem': buyitem,
        'total_price': total_price

    }
  
    return render(request, 'order.html', context)

def update_done_order(request, pk):
    cart = buyItem.objects.get(pk=pk)
    cart.DoneOrder = True
    cart.save()
    return redirect('pos:order')  

@login_required
def reco(request):
    buyitemform = BuyItemForms()  # Instantiate the form
    stocks = Stocks.objects.first()
    drinks = MenuDrinks.objects.filter(menucategory__categorytype='FOOD').order_by('-menuprice1')[:5]
    menuDrinks = MenuDrinks.objects.filter(menucategory__categorytype='DRINKS').order_by('-menuprice1')[:5]
    menuCategory = MenuCategory.objects.all()
    buyitem = buyItem.objects.all()

    current_date = datetime.today()
    top_sale = buyItem.objects.filter(dateordered=current_date).values('buyName').annotate(count=models.Count('buyName')).order_by('-count').first()

    lowest_price = 99999999
    highest_price = 0

    for row in menuDrinks:
        if row.menuprice1 < lowest_price:
            lowest_price = row.menuprice1
        if row.menuprice1 > highest_price:
            highest_price = row.menuprice1

    context = {
        'buyitemform': buyitemform,
        'drinks': drinks,
        'stocks': stocks,
        'menuDrinks': menuDrinks,
        'menuCategory': menuCategory,
        'buyitem': buyitem,
        'lowest_price': lowest_price,
        'highest_price': highest_price,
    }

    return render(request, 'recommendation.html', context)

#cart start
#
@login_required
def cart(request):
    buyitemform = BuyItemForms() 
    stocks = Stocks.objects.first()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory = MenuCategory.objects.all()
    buyitem = buyItem.objects.all()
    total_price = calculate_total_price(buyitem)
    

    context = {
        'buyitemform': buyitemform,
        'stocks': stocks,
        'menuDrinks': menuDrinks,
        'menuCategory': menuCategory,
        'buyitem': buyitem,
        'total_price': total_price

    }
  
  
    return render(request, 'cart.html',context)

def delete_menu_from_cart(request, cart_item_id):
    cart_item = buyItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('pos:cart')

@login_required
def success(request):
    order_number = request.GET.get('order_number')  # Assuming you pass the order number as a query parameter

    context = {
        'order_number': order_number
    }

    return render(request, 'success.html', context)

#cart end
@login_required
def cashier(request):
    buyitemform = BuyItemForms() 
    buyitem = buyItem.objects.all()

    for item in buyitem:
        if item.PWD_discount == 'yes':
            item.AllPayment *= 0.80

    context = {
        'buyitemform': buyitemform,
        'buyitem': buyitem,
    }
    return render(request, 'cashier.html', context)

def update_cashier(request):
    if request.method == 'POST':
        tendered_payment = float(request.POST.get('tendered_payment'))
        item_id = request.POST.get('item_id')
        item = get_object_or_404(buyItem, id=item_id)
        order_number = item.orderNumber
        buy_items = buyItem.objects.filter(orderNumber=order_number)

        # Calculate the total amount for all updated items, including quantity multiplication

        total_buyitems = buy_items.aggregate(
            total=Sum(
                F('buyPrice') * F('buyQuantityMenu') 

            )
        )['total'] or 0.0

        if item.PWD_discount == 'yes':
              total_amount = buy_items.aggregate(
              total=Sum(
            F('buyPrice') * F('buyQuantityMenu') +
            F('menuAOPrice1') * F('buyQuantityMenu') +
            F('menuAOPrice2') * F('buyQuantityMenu') +
            F('menuAOPrice3') * F('buyQuantityMenu') +
            F('menuAOPrice4') * F('buyQuantityMenu') +
            F('menuAOPrice5') * F('buyQuantityMenu')
               )
              )['total'] or 0.0
        else:
            total_amount = buy_items.aggregate(
        total=Sum(
            F('buyPrice') * F('buyQuantityMenu') +
            F('menuAOPrice1') * F('buyQuantityMenu') +
            F('menuAOPrice2') * F('buyQuantityMenu') +
            F('menuAOPrice3') * F('buyQuantityMenu') +
            F('menuAOPrice4') * F('buyQuantityMenu') +
            F('menuAOPrice5') * F('buyQuantityMenu')
        )
    )['total'] or 0.0


        total_add_ons = buy_items.aggregate(
            total=Sum(
                F('menuAOPrice1') * F('buyQuantityMenu') +
                F('menuAOPrice2') * F('buyQuantityMenu') +
                F('menuAOPrice3') * F('buyQuantityMenu') +
                F('menuAOPrice4') * F('buyQuantityMenu') +
                F('menuAOPrice5') * F('buyQuantityMenu')
            )
        )['total'] or 0.0


        for item in buy_items:
            item.buyOrBought = True
            item.tenderedPayment = tendered_payment
            item.dateordered = datetime.now()
            item.save()

        


        if item.PWD_discount == 'yes':
            vat_amount = 0.88 * total_buyitems
            vat_sales = 0.12 * total_buyitems  # Calculate VAT as 88% of the total amount
            discount_amount = 0.20 * total_amount  # Calculate PWD discount as 12% of the total amount
        else:
            vat_amount = 0.00 
            vat_sales = 0.00 # No VAT if PWD discount is not applicable
            discount_amount = 0.00  # No PWD discount if PWD discount is not applicable

        total_payment = total_amount - discount_amount
        change = tendered_payment - total_payment

        context = {
            'dine_option': item.DineIn_Out,  # Assuming `item` represents a single buyItem object
            'order_number': order_number,
            'buy_items': buy_items,
            'total_amount': total_amount,
            'tendered_payment': tendered_payment,
            'change': change,
            'pwd_discount': item.PWD_discount,  # Assuming `item` represents a single buyItem object
            'pwd_id': item.PWD_Id,  
            'vat_amount': vat_amount,  # Include the calculated VAT amount in the context
            'discount_amount': discount_amount,  
            'total_payment': total_payment,
            'total_add_ons': total_add_ons,  # Include the total add-ons amount in the context
            'total_buyitems':total_buyitems,
            'vat_sales': vat_sales,
        }
        return render(request, 'receipt_template.html', context)

    return redirect("pos:cashier")



def delete_order(request, item_id):
    item = get_object_or_404(buyItem, id=item_id)
    item.delete()
    return redirect('pos:cashier')



#computation
def calculate_total_price(buyitem):
    total = 0
    for item in buyitem:
        if not item.transaction and item.total_price:
            total += item.total_price
    rounded_total = round(total, 2)
    return rounded_total

@property
def total_price(self):
    if not self.buyOrBought:
        buyPrice = float(self.buyPrice or 0.0)
        menuAOPrice1 = float(self.menuAOPrice1 or 0.0)
        menuAOPrice2 = float(self.menuAOPrice2 or 0.0)
        menuAOPrice3 = float(self.menuAOPrice3 or 0.0)
        menuAOPrice4 = float(self.menuAOPrice4 or 0.0)
        menuAOPrice5 = float(self.menuAOPrice5 or 0.0)

        return round((buyPrice + menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5) * self.buyQuantityMenu, 2)

    return None # Return 0.0 for already bought items or when the calculation cannot be performed


@login_required
def receipt(request, orderNumber):
    # Retrieve the necessary data based on the order number
    order_items = buyItem.objects.filter(orderNumber=orderNumber)

    # Prepare the receipt data
    receipt_data = {
        'order_number': orderNumber,
        'order_date': order_items.first().dateordered,
        'items': [],
        'total_price': 0,
        'tendered_payment': order_items.first().tenderedPayment,
        'change_amount': 0,
    }

    # Loop through the order items and retrieve the necessary fields
    for item in order_items:
        item_data = {
            'buy_name': item.buyName,
            'buy_price': item.buyPrice,
            'buy_quantity': item.buyQuantityMenu,
            'addons': [],
        }

        # Retrieve addon details
        for i in range(1, 6):
            addon_name = getattr(item, f'buyAddOns{i}', None)
            addon_price = getattr(item, f'menuAOPrice{i}', None)
            if addon_name is not None and addon_price is not None:
                item_data['addons'].append({'addon': addon_name, 'price': addon_price})

        receipt_data['items'].append(item_data)

        if item.buyPrice is not None and item.buyQuantityMenu is not None:
            receipt_data['total_price'] += item.buyPrice * item.buyQuantityMenu

    # Calculate the change amount
    receipt_data['change_amount'] = receipt_data['tendered_payment'] - receipt_data['total_price']

    return render(request, 'receipt.html', {'receipt_data': receipt_data})


@login_required
def Mcashier(request):
    buyitemform = BuyItemForms() 
    buyitem = buyItem.objects.all()

    for item in buyitem:
        if item.PWD_discount == 'yes':
            item.AllPayment *= 0.80

    context = {
        'buyitemform': buyitemform,
        'buyitem': buyitem,
    }
    return render(request, 'MCashier.html', context)


from django.shortcuts import get_object_or_404


@login_required
def Mupdate_cashier(request):
    if request.method == 'POST':
        tendered_payment = float(request.POST.get('tendered_payment'))
        item_id = request.POST.get('item_id')
        item = get_object_or_404(buyItem, id=item_id)
        order_number = item.orderNumber
        buy_items = buyItem.objects.filter(orderNumber=order_number)

        # Calculate the total amount for all updated items, including quantity multiplication

        total_buyitems = buy_items.aggregate(
            total=Sum(
                F('buyPrice') * F('buyQuantityMenu') 

            )
        )['total'] or 0.0

        if item.PWD_discount == 'yes':
              total_amount = buy_items.aggregate(
              total=Sum(
            F('buyPrice') * F('buyQuantityMenu') +
            F('menuAOPrice1') * F('buyQuantityMenu') +
            F('menuAOPrice2') * F('buyQuantityMenu') +
            F('menuAOPrice3') * F('buyQuantityMenu') +
            F('menuAOPrice4') * F('buyQuantityMenu') +
            F('menuAOPrice5') * F('buyQuantityMenu')
               )
              )['total'] or 0.0
        else:
            total_amount = buy_items.aggregate(
        total=Sum(
            F('buyPrice') * F('buyQuantityMenu') +
            F('menuAOPrice1') * F('buyQuantityMenu') +
            F('menuAOPrice2') * F('buyQuantityMenu') +
            F('menuAOPrice3') * F('buyQuantityMenu') +
            F('menuAOPrice4') * F('buyQuantityMenu') +
            F('menuAOPrice5') * F('buyQuantityMenu')
        )
    )['total'] or 0.0


        total_add_ons = buy_items.aggregate(
            total=Sum(
                F('menuAOPrice1') * F('buyQuantityMenu') +
                F('menuAOPrice2') * F('buyQuantityMenu') +
                F('menuAOPrice3') * F('buyQuantityMenu') +
                F('menuAOPrice4') * F('buyQuantityMenu') +
                F('menuAOPrice5') * F('buyQuantityMenu')
            )
        )['total'] or 0.0


        for item in buy_items:
            item.buyOrBought = True
            item.tenderedPayment = tendered_payment
            item.dateordered = datetime.now()
            item.save()

        


        if item.PWD_discount == 'yes':
            vat_amount = 0.88 * total_buyitems
            vat_sales = 0.12 * total_buyitems  # Calculate VAT as 88% of the total amount
            discount_amount = 0.20 * total_buyitems  # Calculate PWD discount as 12% of the total amount
        else:
            vat_amount = 0.00 
            vat_sales = 0.00 # No VAT if PWD discount is not applicable
            discount_amount = 0.00  # No PWD discount if PWD discount is not applicable

        total_payment = total_amount - discount_amount
        change = tendered_payment - total_payment

        context = {
            'dine_option': item.DineIn_Out,  # Assuming `item` represents a single buyItem object
            'order_number': order_number,
            'buy_items': buy_items,
            'total_amount': total_amount,
            'tendered_payment': tendered_payment,
            'change': change,
            'pwd_discount': item.PWD_discount,  # Assuming `item` represents a single buyItem object
            'pwd_id': item.PWD_Id,  
            'vat_amount': vat_amount,  # Include the calculated VAT amount in the context
            'discount_amount': discount_amount,  
            'total_payment': total_payment,
            'total_add_ons': total_add_ons,  # Include the total add-ons amount in the context
            'total_buyitems':total_buyitems,
            'vat_sales': vat_sales,
        }
        return render(request, 'Mreceipt.html', context)

    return redirect("pos:Mcashier")

def Mdelete_order(request, item_id):
    item = get_object_or_404(buyItem, id=item_id)
    item.delete()
    return redirect('pos:Mcashier')

@login_required
def Morder(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id:
            item = buyItem.objects.get(pk=item_id)
            item.delete()
            return redirect('pos:Morder')
    
    buyitemform = BuyItemForms() 
    stocks = Stocks.objects.first()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory = MenuCategory.objects.all()
    buyitem = buyItem.objects.all()
    total_price = calculate_total_price(buyitem)

    context = {
        'buyitemform': buyitemform,
        'stocks': stocks,
        'menuDrinks': menuDrinks,
        'menuCategory': menuCategory,
        'buyitem': buyitem,
        'total_price': total_price
    }
  
    return render(request, 'Morder.html', context)

def Mupdate_done_order(request, pk):
    cart = buyItem.objects.get(pk=pk)
    cart.DoneOrder = True
    cart.save()
    return redirect('pos:Morder')  
    
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_all_payments(request):
    if request.method == 'POST':
        order_number = request.POST.get('order_number')
        payment_amount = request.POST.get('payment_amount')
        
        # Update the AllPayment field for items with the specified order number
        items = buyItem.objects.filter(orderNumber=order_number)
        for item in items:
            item.AllPayment = payment_amount
            item.save()
        
        return JsonResponse({'message': 'AllPayment updated successfully.'})
    
    return JsonResponse({'message': 'Invalid request.'})