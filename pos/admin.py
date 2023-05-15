from django.contrib import admin
from .models import Stocks
from .models import MenuCategory
from .models import MenuDrinks


class StocksAdmin(admin.ModelAdmin):
    list_display = ("stockname", "stockmeasurement", "stockcategory", "stockquantity", "stockprice", "stockdate_in", "stockexpiration")


class MenucategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "categorytype")

class MenuDrinksAdmin(admin.ModelAdmin):
    list_display = ("menucategory", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5", "menuIngrPrice1", "menuIngrPrice2", "menuIngrPrice3", "menuIngrPrice4", "menuIngrPrice5", "menuname", "menuimage", "menuprice", "sugarlevel","alcohollevel", "ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5", "addons1", "addons2", "addons3", "addons4", "addons5",
                    "hotAndCold", "quantityIng1", "quantityIng2", "quantityIng3", "quantityIng4", "quantityIng5", "quantityAO1", "quantityAO2", "quantityAO3", "quantityAO4", "quantityAO5" )

admin.site.register(Stocks, StocksAdmin)
admin.site.register(MenuCategory,MenucategoryAdmin,)
admin.site.register(MenuDrinks, MenuDrinksAdmin)