from django.db import models


STOCK_CATEGORY = (
    ("INGR", "Ingredients"),
    ("AO", "AddOns"),
    ("UTNSL", "Utensils"),
)

STOCK_QUANTITY = (
    ("G", "Grams"),
    ("PCS", "Pieces"),
    ("ML", "MiliLiters"),
)



class Stocks(models.Model):
    stockname = models.CharField(max_length=50)
    stockcategory = models.CharField(choices=STOCK_CATEGORY, max_length=100)
    stockdate_in = models.DateField()
    stockexpiration = models.DateField()

    def __str__(self):
        return self.stockname
# END STOCKS


# MENU START
TYPES_MENU = (
    ("DRINKS", "Drinks"),
    ("FOOD", "Food"),
)


class MenuCategory (models.Model):
    name = models.CharField(max_length=100)
    categorytype = models.CharField(choices=TYPES_MENU, max_length=100)

    def __str__(self):
        return self.name


class MenuDrinks (models.Model):
    menucategory = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE)
    menuname = models.CharField(max_length=100)
    menuAOPrice1 = models.FloatField( null=True, blank=True)
    menuAOPrice2 = models.FloatField( null=True, blank=True)
    menuAOPrice3 = models.FloatField( null=True, blank=True)
    menuAOPrice4 = models.FloatField( null=True, blank=True)
    menuAOPrice5 = models.FloatField( null=True, blank=True)
    menuimage = models.ImageField(upload_to="mema/")
    menuprice1 = models.FloatField(null=True, blank=True)
    menuprice2 = models.FloatField(null=True, blank=True)
    menuprice3 = models.FloatField(null=True, blank=True)
    ingredient1 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient1', null=True, blank=True)
    ingredient2 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient2', null=True, blank=True)
    ingredient3 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient3', null=True, blank=True)
    ingredient4 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient4', null=True, blank=True)
    ingredient5 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient5', null=True, blank=True)    
    ingredient6 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient6', null=True, blank=True)
    ingredient7 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient7', null=True, blank=True)
    ingredient8 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient8', null=True, blank=True)
    ingredient9 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient9', null=True, blank=True)
    ingredient10 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient10', null=True, blank=True)
    addons1 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons1', null=True, blank=True)
    addons2 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons2', null=True, blank=True)
    addons3 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons3', null=True, blank=True)
    addons4 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons4', null=True, blank=True)
    addons5 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons5', null=True, blank=True)
    q1 = models.BooleanField (default= False)
    q2 = models.BooleanField (default= False)
    q3 = models.BooleanField (default= False)
    question1 = models.BooleanField (default= False)
    question2 = models.BooleanField (default= False)
    question3 = models.BooleanField (default= False)
    question4 = models.BooleanField (default= False)

    def __str__(self):
        return f"{self.menuname} ({self.menucategory.name})"

#HOME START


PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('gcash', 'GCash'),
    )

IN_OUT = (
        ('IN', 'Dine In'),
        ('OUT', 'Dine Out'),
    )
DISCOUNT = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )

class buyItem(models.Model):
    buyName= models.CharField (max_length=255, null=True, blank=True)
    buySize = models.CharField(max_length=15, null=True, blank=True)
    buyQuantityMenu = models.PositiveIntegerField (null=True, blank=True)
    buyPrice = models.FloatField (null=True, blank=True)
    buyAddOns1 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns2 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns3 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns4 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns5 = models.CharField (max_length=255, null=True, blank=True)
    menuAOPrice1 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice2 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice3 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice4 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice5 = models.FloatField(default=0,null=True, blank=True)
    buyingredient1 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient2 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient3 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient4 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient5 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient6 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient7 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient8 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient9 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient10 = models.CharField (max_length=255, null=True, blank=True)
    transaction = models.BooleanField(default=False)
    buyOrBought = models.BooleanField(default=False)
    DoneOrder = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES, null=True, blank=True)
    DineIn_Out = models.CharField(max_length=255, choices=IN_OUT, null=True, blank=True)
    AllPayment = models.FloatField(null=True, blank=True)
    tenderedPayment = models.FloatField(null=True, blank=True)
    orderNumber = models.PositiveIntegerField (null=True, blank=True)
    dateordered = models.DateTimeField (null=True, blank=True)
    priceSize = models.FloatField( null=True, blank=True)
    PWD_discount = models.CharField(max_length=255, choices=DISCOUNT, null=True, blank=True)
    PWD_Id = models.CharField (max_length=12, null=True, blank=True)

    @property
    def total_price(self):
        if not self.buyOrBought:
            buyPrice = self.buyPrice or 0.0
            menuAOPrice1 = self.menuAOPrice1 or 0.0
            menuAOPrice2 = self.menuAOPrice2 or 0.0
            menuAOPrice3 = self.menuAOPrice3 or 0.0
            menuAOPrice4 = self.menuAOPrice4 or 0.0
            menuAOPrice5 = self.menuAOPrice5 or 0.0

            return round((buyPrice + menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5) * self.buyQuantityMenu, 2)


@property
def total_AO(self):
    menuAOPrice1 = self.menuAOPrice1 or 0.0
    menuAOPrice2 = self.menuAOPrice2 or 0.0
    menuAOPrice3 = self.menuAOPrice3 or 0.0
    menuAOPrice4 = self.menuAOPrice4 or 0.0
    menuAOPrice5 = self.menuAOPrice5 or 0.0
    
    if self.buyOrBought and menuAOPrice1 and menuAOPrice2 and menuAOPrice3 and menuAOPrice4 and menuAOPrice5:
        total_AO = menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5
        return round(total_AO, 2)
    
    return round(menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5, 2)


@property
def AllPayment(self):
    if not self.buyOrBought:
        total_price = self.total_price or 0.0
        total_AO = self.total_AO or 0.0

        return round(total_price + total_AO, 2)
    return 0.0

