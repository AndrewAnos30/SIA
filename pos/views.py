from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Stocks, STOCK_CATEGORY, STOCK_QUANTITY
from .models import MenuCategory, MenuDrinks, TYPES_MENU
from .models import buyItem
from pos import views
from .forms import IngridientsForm, AddOnsForm, UtensilsForm
from .forms import MenuCategoryForm, MenuDrinksForm
from .forms import BuyItemForms
import logging, random, datetime
from itertools import groupby


def base(request):
  
    return render(request, 'base.html')

#inventory start
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
            print("puta")
            form.save()
            return HttpResponseRedirect(reverse("pos:home"))
        else:
            print(form.errors)  # Check for any form errors in the console

    return HttpResponseRedirect(reverse("pos:home"))



#home end

def index(request):
  
    return render(request, 'index.html')


def sales(request):
   
    buyitem = buyItem.objects.all()
    

    context = {
 
    'buyitem': buyitem,
    }
    return render(request, 'sales.html', context)


def order(request):
  
    return render(request, 'order.html')



def reco(request):
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
  
    return render(request, 'recommendation.html', context)

def buy_item_drinks1(request):
    if request.method == 'POST':
        form = BuyItemForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pos:home"))
        else:
            print(form.errors)  # Check for any form errors in the console

    return HttpResponseRedirect(reverse("pos:reco"))







#cart start
#
#
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


def update_values(request):
    if request.method == 'POST':
        # Get the form data from the request
        payment_method = request.POST.get('payment_method')
        dine_in_out = request.POST.get('DineIn_Out')
        tendered_payment = request.POST.get('tenderedPayment')
        AllPayment = float(request.POST.get('AllPayment'))

        # Generate a unique order number
        order_number = str(random.randint(1, 99999)).zfill(5)

        # Get only the buyItem objects with buyOrBought=False
        buy_items = buyItem.objects.filter(buyOrBought=False)
      
        # Get the current date and time
        current_datetime = datetime.datetime.now()

        for item in buy_items:
            # Update the fields for each buyItem object
            item.payment_method = payment_method
            item.DineIn_Out = dine_in_out
            item.tenderedPayment = tendered_payment
            item.AllPayment = AllPayment
            if not item.buyOrBought:
                item.orderNumber = order_number
                item.buyOrBought = True  # Set buyOrBought to True
                item.dateordered = current_datetime  # Store the current date and time
            # Save the changes for each buyItem object
            item.save()

        # Redirect to a success page or do any further processing
        return redirect("pos:home")

    # Render the form
    return render(request, "home.html")




#forgroupings
#cart end


#computation
def calculate_total_price(buyitem):
    total = 0
    for item in buyitem:
        if not item.buyOrBought and item.total_price:
            total += item.total_price
    rounded_total = round(total, 2)
    return rounded_total