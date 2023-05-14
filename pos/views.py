from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Stocks, STOCK_CATEGORY, STOCK_QUANTITY
from .models import MenuCategory, MenuDrinks

from .forms import IngridientsForm, AddOnsForm, UtensilsForm
from .forms import MenuCategoryForm, MenuDrinksForm

def base(request):
  
    return render(request, 'base.html')

#inventory start
def inventory(request):
    ingridientForm = IngridientsForm()
    my_data_ingredients = Stocks.objects.all()
    my_data_addOns = Stocks.objects.all()
    my_data_utensils = Stocks.objects.all()
    addOnsForm = AddOnsForm()
    utensilsForm = UtensilsForm()

    context = {
        "stock_category": STOCK_CATEGORY,
        "stock_quantity": STOCK_QUANTITY,
        "my_data_i" : my_data_ingredients.filter(stockcategory="INGR"),
        "my_data_a" : my_data_addOns.filter(stockcategory="AO"),
        "my_data_u" : my_data_utensils.filter(stockcategory="UTNSL"),
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
#inventory end

def menu(request):
    menucategoryform = MenuCategoryForm   
    mcategory = MenuCategory.objects.all()
    menudrinksform = MenuDrinksForm
    stocks = Stocks.objects.all()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory= MenuCategory.objects.all()

    
    context ={
    "menucategoryform" : menucategoryform,
    "mcategory" : mcategory,
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

import logging

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
#MENU END

#HOME START
def home(request):

    menucategoryform = MenuCategoryForm   
    menudrinksform = MenuDrinksForm
    stocks = Stocks.objects.first()
    menuDrinks = MenuDrinks.objects.all()
    menuCategory= MenuCategory.objects.all()

    
    context ={
    "menucategoryform" : menucategoryform,
    "menudrinksform" : menudrinksform,
    "stocks" : stocks,
    "menuDrinks" : menuDrinks,
    "menuCategory" : menuCategory,
    }
    return render(request, 'home.html',context)

#menu end

def index(request):
  
    return render(request, 'index.html')


def sales(request):
  
    return render(request, 'sales.html')


def order(request):
  
    return render(request, 'order.html')

def reco(request):
  
    return render(request, 'recommendation.html')

def reco(request):
  
    return render(request, 'recommendation.html')

def cart(request):
  
    return render(request, 'cart.html')