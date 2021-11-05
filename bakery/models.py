import uuid
from django.db import models

# Create your models here.
class ingredients(models.Model):
    ingredient=models.CharField(max_length=100,default="Some Ingredient")
    quantity=models.IntegerField()
    rate=models.IntegerField(default=1)

    def __str__(self):
        return self.ingredient;

class product(models.Model):
    product_name=models.CharField(max_length=200,default="")
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    SP=models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

    def getAllIngredients(self):
        temp=recipe.objects.filter(product=self)
        return temp

class recipe(models.Model):
    product=models.ForeignKey(product,related_name="product",on_delete=models.CASCADE)
    ingredient=models.ForeignKey(ingredients,related_name="ingredients",on_delete=models.CASCADE)
    amount_required=models.IntegerField()

    def CP(self):
        return self.amount_required*(self.ingredient.rate)

    def in_stock(self):
        return int(self.ingredient.quantity/self.amount_required)

    def buy(self,freq):
        return int(self.ingredient.quantity-(freq*self.amount_required))
        # self.save()
        # return 0

    def __str__(self):
        return str(self.product)+"-"+str(self.ingredient)