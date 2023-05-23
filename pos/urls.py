from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pos'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('/inventory/', views.inventory, name='inventory'),
    path('/menu/', views.menu, name='menu'),
    path('order', views.order, name='order'),
    path('sales', views.sales, name='sales'),
    path('home/', views.home, name='home'),
    path('reco/', views.reco, name='reco'),
    path('/cart/', views.cart, name='cart'),
    path('add_ingridients', views.addIngridients, name='add_ingridients'),
    path('add_addOns', views.addAddOns, name='add_addOns'),
    path('add_utensils', views.addUtensils, name='add_utensils'),
    path('add_menuCategory', views.addMenuCategory, name='add_menuCategory'),
    path('add_menuDrinks', views.addMenuDrinks, name='add_menuDrinks'),
    path('edit_menuCategory', views.edit_menu_category, name='edit_menuCategory'),
    path('update_stock', views.update_stock, name='update_stock'), 
    path('delete_stock', views.delete_stock, name='delete_stock'),   
    path('delete_category', views.delete_category, name='delete_category'),
    path('delete_menu/<int:menu_id>/', views.delete_menu, name='delete_menu'), 
    path('buyitemdrinks/', views.buy_item_drinks, name='buyitemdrinks'),
    path('buy_item_drinks1/', views.buy_item_drinks1, name='buy_item_drinks1'),
    path('update_values', views.update_values, name='update_values'),
    path('update_done_order/<int:pk>/', views.update_done_order, name='update_done_order'),
    path('receipt/<int:orderNumber>/', views.receipt, name='receipt'),
    path('cart/delete/<int:cart_item_id>/', views.delete_menu_from_cart, name='delete_menu_from_cart'),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)