from django.contrib import admin
from .models import Stocks
from .models import MenuCategory
from .models import MenuDrinks
from .models import buyItem


class StocksAdmin(admin.ModelAdmin):
    list_display = ("stockname", "stockmeasurement", "stockcategory", "stockquantity", "stockdate_in", "stockexpiration")


class MenucategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "categorytype")

class MenuDrinksAdmin(admin.ModelAdmin):
    list_display = ("menucategory","menuname","menuprice", "hotAndCold", "menuimage", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5", "ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5", "addons1", "addons2", "addons3", "addons4", "addons5",
                     "quantityIng1", "quantityIng2", "quantityIng3", "quantityIng4", "quantityIng5", "quantityAO1", "quantityAO2", "quantityAO3", "quantityAO4", "quantityAO5" )


class BuyItemAdmin(admin.ModelAdmin):
    list_display = ("buyOrBought","buySize","priceSize" , "buyQuantityMenu", "buyName", "buyPrice", "buyQuantityAO1", "buyQuantityAO2", "buyQuantityAO3", "buyQuantityAO4", "buyQuantityAO5", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5", "buyAddOns1", "buyAddOns2", "buyAddOns3", "buyAddOns4", "buyAddOns5",
                      "buyingredient1", "buyingredient2", "buyingredient3", "buyingredient4", "buyingredient5", "buyQuantityIng1", "buyQuantityIng2", "buyQuantityIng3", "buyQuantityIng4", "buyQuantityIng5", "payment_method", "DineIn_Out", "AllPayment", "tenderedPayment", "orderNumber", "dateordered", "DoneOrder")

admin.site.register(Stocks, StocksAdmin)
admin.site.register(MenuCategory,MenucategoryAdmin)
admin.site.register(MenuDrinks, MenuDrinksAdmin)
admin.site.register(buyItem, BuyItemAdmin)