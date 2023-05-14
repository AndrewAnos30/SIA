from django import forms

# Mga database
from .models import Stocks, STOCK_CATEGORY, STOCK_QUANTITY
from .models import MenuCategory, MenuDrinks, TYPES_MENU

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
        fields = ["stockname","stockmeasurement", "stockcategory", "stockquantity", "stockprice", "stockdate_in", "stockexpiration"]


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
        fields = ["stockname","stockmeasurement", "stockcategory", "stockquantity", "stockprice", "stockdate_in", "stockexpiration"]


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
        fields = ["stockname","stockmeasurement", "stockcategory", "stockquantity", "stockprice", "stockdate_in", "stockexpiration"]
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
        fields = ["menucategory", "menuname","menuprice", "menuimage", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5", "menuIngrPrice1", "menuIngrPrice2", "menuIngrPrice3", "menuIngrPrice4", "menuIngrPrice5", "sugarlevel", "alcohollevel","ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5", "addons1", "addons2", "addons3", "addons4","addons5"]
        widgets = {
            'sugarlevel': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'alcohollevel': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No')))
           
        }

