from django import forms

# Mga database
from .models import Stocks, STOCK_CATEGORY, STOCK_QUANTITY
from .models import MenuCategory, MenuDrinks, TYPES_MENU
from .models import buyItem

#stocks start
class IngridientsForm(forms.ModelForm):
    stockcategory = forms.ChoiceField(
        choices=STOCK_CATEGORY,
        widget=forms.RadioSelect,
    )
    stockmeasurement = forms.ChoiceField(
        choices=STOCK_QUANTITY,
        widget=forms.RadioSelect,
    )


    class Meta:
        model = Stocks  # Eto yung table na gagamitin
        fields = ["stockname","stockmeasurement", "stockcategory", "stockquantity", "stockdate_in", "stockexpiration"]


class AddOnsForm(forms.ModelForm):
    stockcategory = forms.ChoiceField(
        choices=STOCK_CATEGORY,
        widget=forms.RadioSelect,
    )

    stockmeasurement = forms.ChoiceField(
        choices=STOCK_QUANTITY,
        widget=forms.RadioSelect,
    )



    class Meta:
        model = Stocks  # Eto yung table na gagamitin
        fields = ["stockname","stockmeasurement", "stockcategory", "stockquantity", "stockdate_in", "stockexpiration"]

class UtensilsForm(forms.ModelForm):
    stockcategory = forms.ChoiceField(
        choices=STOCK_CATEGORY,
        widget=forms.RadioSelect,
    )
    stockmeasurement = forms.ChoiceField(
        choices=STOCK_QUANTITY,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Stocks  
        fields = ["stockname","stockmeasurement", "stockcategory", "stockquantity", "stockdate_in", "stockexpiration"]
#stocks end


#menu start
class MenuCategoryForm(forms.ModelForm):
    categorytype = forms.ChoiceField(
        choices=TYPES_MENU,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = MenuCategory
        fields = ["name","categorytype"]


class MenuDrinksForm(forms.ModelForm):
    class Meta:
        model = MenuDrinks
        fields = ["hotAndCold", "menucategory", "menuname","menuprice", "menuimage", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5","ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5", "addons1", "addons2", "addons3", "addons4","addons5", "quantityIng1", "quantityIng2", "quantityIng3", "quantityIng4", "quantityIng5", "quantityAO1", "quantityAO2", "quantityAO3", "quantityAO4", "quantityAO5"]
        widgets = {
            'sugarlevel': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'alcohollevel': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'hotAndCold': forms.RadioSelect(choices=(('hot', 'Hot'), ('cold', 'Cold'), ('hot and cold', 'Both'))),           
        }
#Menu End

#home Start

class BuyItemForms(forms.ModelForm):
    class Meta:
        model = buyItem
        fields = [
        "buyOrBought","buySize","buyQuantityMenu", "buyName", "buyPrice","buyAddOns1","buyAddOns2","buyAddOns3","buyAddOns4","buyAddOns5", "buyQuantityAO1", "buyQuantityAO2", "buyQuantityAO3", "buyQuantityAO4", "buyQuantityAO5", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5",
        "buyingredient1", "buyingredient2", "buyingredient3", "buyingredient4", "buyingredient5", "buyQuantityIng1", "buyQuantityIng2", "buyQuantityIng3", "buyQuantityIng4", "buyQuantityIng5"
        ]
        widgets = {
            'buySize': forms.RadioSelect(choices=(('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'))),
        }
