from django import forms
from django.contrib.auth.models import User
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

    class Meta:
        model = Stocks
        fields = ["stockname", "stockcategory", "stockdate_in", "stockexpiration"]


class AddOnsForm(forms.ModelForm):
    stockcategory = forms.ChoiceField(
        choices=STOCK_CATEGORY,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Stocks
        fields = ["stockname", "stockcategory", "stockdate_in", "stockexpiration"]


class UtensilsForm(forms.ModelForm):
    stockcategory = forms.ChoiceField(
        choices=STOCK_CATEGORY,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Stocks
        fields = ["stockname", "stockcategory", "stockdate_in", "stockexpiration"]
#stocks end


#menu start
class MenuCategoryForm(forms.ModelForm):
    categorytype = forms.ChoiceField(
        choices=TYPES_MENU,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = MenuCategory
        fields = ["name", "categorytype"]


class MenuDrinksForm(forms.ModelForm):
    class Meta:
        model = MenuDrinks
        fields = [ "menucategory", "menuname", "menuimage", "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5", "ingredient1", "ingredient2", "ingredient3", "ingredient4", "ingredient5", "ingredient6", "ingredient7", "ingredient8", "ingredient9", "ingredient10", "addons1", "addons2", "addons3", "addons4", "addons5", "menuprice1", "menuprice2", "menuprice3", "question1", "question2", "question3", "question4", "q1", "q2", "q3"]
        widgets = {
            'q1': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'q2': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'q3': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question1': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question2': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question3': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question4': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
        }

#Menu End

#home Start

class BuyItemForms(forms.ModelForm):
  
    class Meta:
        model = buyItem
        fields = [
            "transaction", "buyOrBought", "buySize", "buyQuantityMenu", "buyName", "buyPrice",
            "buyAddOns1", "buyAddOns2", "buyAddOns3", "buyAddOns4", "buyAddOns5",
            "menuAOPrice1", "menuAOPrice2", "menuAOPrice3", "menuAOPrice4", "menuAOPrice5",
            "buyingredient1", "buyingredient2", "buyingredient3", "buyingredient4", "buyingredient5",
            "buyingredient6", "buyingredient7", "buyingredient8", "buyingredient9", "buyingredient10",
            "payment_method", "DineIn_Out", "AllPayment", "tenderedPayment", "orderNumber", "dateordered", "DoneOrder",
            "priceSize", "PWD_discount", "PWD_Id"
        ]
        widgets = {
            'payment_method': forms.RadioSelect(choices=(('cash', 'Cash'), ('gcash', 'GCash'))),
            'DineIn_Out': forms.RadioSelect(choices=(('IN', 'Dine In'), ('OUT', 'Dine Out'))),
            'PWD_discount': forms.RadioSelect(choices=(('yes', 'YES'), ('no', 'NO'))),
        }
