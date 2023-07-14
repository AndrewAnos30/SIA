from django.contrib import admin
from .models import Stocks, MenuCategory, MenuDrinks, buyItem


class StocksAdmin(admin.ModelAdmin):
    list_display = ("stockname", "stockcategory", "stockdate_in", "stockexpiration")


class MenucategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "categorytype")


class MenuDrinksAdmin(admin.ModelAdmin):
    list_display = (
        "menucategory",
        "menuname",
        "menuimage",
        "menuprice1",
        "menuprice2",
        "menuprice3",
        "menuAOPrice1",
        "menuAOPrice2",
        "menuAOPrice3",
        "menuAOPrice4",
        "menuAOPrice5",
        "ingredient1",
        "ingredient2",
        "ingredient3",
        "ingredient4",
        "ingredient5",
        "ingredient6",
        "ingredient7",
        "ingredient8",
        "ingredient9",
        "ingredient10",
        "addons1",
        "addons2",
        "addons3",
        "addons4",
        "addons5",
        "question1",
        "question2",
        "question3",
        "question4",
        "q1",
        "q2",
        "q3"
    )
        


class BuyItemAdmin(admin.ModelAdmin):
    list_display = ("PWD_Id","PWD_discount","transaction", "buyOrBought", "buySize", "priceSize", "buyQuantityMenu", "buyName", "buyPrice", "buyAddOns1", "buyAddOns2", "buyAddOns3", "buyAddOns4", "buyAddOns5", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5", "buyingredient1", "buyingredient2", "buyingredient3", "buyingredient4", "buyingredient5", "payment_method", "DineIn_Out", "AllPayment", "tenderedPayment", "orderNumber", "dateordered", "DoneOrder", "buyingredient6", "buyingredient7", "buyingredient8", "buyingredient9", "buyingredient10")


admin.site.register(Stocks, StocksAdmin)
admin.site.register(MenuCategory, MenucategoryAdmin)
admin.site.register(MenuDrinks, MenuDrinksAdmin)
admin.site.register(buyItem, BuyItemAdmin)
