from rest_framework import serializers
from .models import *

class ingredientInv(serializers.ModelSerializer):
    class Meta:
        model=ingredients
        fields="__all__"


    def update(self,instance,validated_data):
        quantity_="quantity"
        rate_="rate"
        if quantity_ in validated_data.keys():
            instance.quantity+=validated_data[quantity_]
        if rate_ in validated_data.keys():
            instance.rate=validated_data[rate_]
        instance.save()
        return ingredientInv(instance)

class recipeInv(serializers.ModelSerializer):
    ingredient=ingredientInv(read_only=True)
    CP=serializers.SerializerMethodField()
    in_stock=serializers.SerializerMethodField()
    class Meta:
        model=recipe
        fields=['ingredient','amount_required','CP','in_stock']

    def get_CP(self,obj):
        return obj.CP()
    def get_in_stock(self,obj):
        return obj.in_stock()


class productInv(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()
    CP=serializers.SerializerMethodField()
    in_stock=serializers.SerializerMethodField()
    class Meta:
        model=product
        fields=["product_name","id","ingredients","SP","CP","in_stock"]

    def get_ingredients(self,obj):
        return recipeInv(obj.getAllIngredients(),many=True).data

    def get_in_stock(self,obj):
        arr=list()
        for i in self.get_ingredients(obj):
            temp=i['in_stock']
            arr.append(temp)
        return int(min(arr))

    def get_CP(self,obj):
        CP="CP"
        sum=0
        for i in self.get_ingredients(obj):
            sum+=i[CP]
        return sum
    def update(self, instance, validated_data):
        product_name="product_name"
        SP="SP"
        if product_name in validated_data.keys():
            instance.product_name=validated_data[product_name]
        if SP in validated_data.keys():
            instance.SP=validated_data[SP]
        instance.save()
        return productInv(instance).data

# ________________________________Customer_Serialisers______________________________________________________________________

class Market(serializers.ModelSerializer):

    in_stock=serializers.SerializerMethodField()
    class Meta:
        model = product
        fields = ["product_name","id","SP","in_stock"]

    def get_ingredients(self,obj):
        return recipeInv(obj.getAllIngredients(),many=True).data

    def get_in_stock(self,obj):
        arr=list()
        for i in self.get_ingredients(obj):
            temp=i['in_stock']
            arr.append(temp)
        return int(min(arr))