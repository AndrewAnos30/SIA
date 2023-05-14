
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pos'

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('/inventory/', views.inventory, name='inventory'),
    path('/menu/', views.menu, name='menu'),
    path('order', views.order, name='order'),
    path('sales', views.sales, name='sales'),
    path('home', views.home, name='home'),
    path('reco', views.reco, name='reco'),
    path('/cart/', views.cart, name='cart'),
    path('add_ingridients', views.addIngridients, name='add_ingridients'),
    path('add_addOns', views.addAddOns, name='add_addOns'),
    path('add_utensils', views.addUtensils, name='add_utensils'),
    path('add_menuCategory', views.addMenuCategory, name='add_menuCategory'),
    path('add_menuDrinks', views.addMenuDrinks, name='add_menuDrinks'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)