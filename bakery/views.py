from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny ,IsAdminUser
from .serializers import *
from Customer.serializers import *
from rest_framework import status
from Customer.models import *

# _______________________________ADMIN_VIEWS________________________________________________________________________

class inventoryRecipe(APIView):
    permission_classes = [IsAdminUser,]
    def get(self, request):
        id="id"
        products_="products"
        if id in request.query_params:
            if(product.objects.filter(id=request.query_params[id]).exists()):
                productU=product.objects.get(id=request.query_params[id])
                result=productInv(productU)
        else:
            temp=product.objects.all()
            result=productInv(temp,many=True)
        return (Response({products_:result.data},status=status.HTTP_200_OK))

    def addIngredients(self,instance,data):
        ingredients_="ingredients"
        ingredient_="id"
        amount_="amount_required"
        for i in data[ingredients_]:
            ingredientU = ingredients.objects.get(id=i[ingredient_])
            amount = i[amount_]
            temp = recipe.objects.create(product=instance, ingredient=ingredientU, amount_required=amount)

    def post(self, request):
        id="id"
        ingredient_list="ingredients"
        name="product_name"
        # Constants Defined
        if id in request.data:
            if(product.objects.filter(id=request.data[id]).exists()):
                productU=product.objects.get(id=request.data[id])
                temp=productInv()
                temp.update(productU,request.data)
                if ingredient_list in request.data:
                    recipe.objects.filter(product=productU).delete()
                    self.addIngredients(productU,request.data)
                result = productInv(productU)
                return Response({"MSG":result.data})
            else:
                return (Response({"MSG": "Invalid"}))
        elif ingredient_list and name in request.data:
            productU=product.objects.create(product_name=request.data[name])
            self.addIngredients(productU, request.data)
            result = productInv(productU)
            return Response({"MSG":result.data})
        else:
            return (Response({"MSG": "Invalid"}))
#
    def delete(self, request):
        id_="id"
        msg_="msg"
        success_msg="Product Deleted"
        error_msg="Problem with JSON or no such Product"
        if id_ in request.data:
            id=request.data[id_]
            if(product.objects.filter(id=id).exists()):
                product.objects.get(id=id).delete()
                return Response({msg_:success_msg},status=status.HTTP_200_OK)
            else:
                return Response({msg_:error_msg}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({msg_:error_msg}, status=status.HTTP_400_BAD_REQUEST)


class inventoryIngred(APIView):
    permission_classes = [IsAdminUser,]
    def get(self, request):
        id_='id'
        search='search'
        ingredients_='ingredients'
        error_msg="Invalid ID"
        msg_="msg"
        # Constants Defined
        if id_ in request.query_params:
            id=request.query_params.get(id_)
            if(ingredients.objects.filter(id=id).exists()):
                ingred = ingredientInv(ingredients.objects.get(id=id))
            else:
                return (Response({msg_:error_msg},status=status.HTTP_400_BAD_REQUEST))
        elif search in request.query_params:
            ingred = ingredientInv(ingredients.objects.filter(ingredient__contains=request.query_params.get(search)),many=True)
        else:
            ingred=ingredientInv(ingredients.objects.all(),many=True)
        return(Response({ingredients_:ingred.data},status=status.HTTP_200_OK))

    def post(self, request):
        id_ = 'id'
        ingredient_ = 'ingredient'
        Data_='data'
        # Constants Defined
        flag=True
        idPresent=True
        if id_ not in request.POST.keys():
            id=0
            idPresent=False
        else:
            id=request.data[id_]
        if (ingredients.objects.filter(Q(ingredient=request.data[ingredient_]) | Q(id=id)).exists()):
            # The above statement checks if the ingredient with the same name exists or with that particular id
            # if id is provided
            # This helps in reducing in errorful redundancy data population
            ingred = ingredientInv()
            if (idPresent):
                data=ingred.update(ingredients.objects.get(id=id), request.data)
            else:
                data=ingred.update(ingredients.objects.get(ingredient=request.data[ingredient_]), request.data)
            flag=False
            #flag becomes false, as in not to create a new element
        else:
            ingred=ingredientInv(data=request.data)
        if(flag and ingred.is_valid()):
            ingred.save()
            data=ingred
        return(Response({Data_:data.data,},status=status.HTTP_201_CREATED))

    def delete(self, request):
        if(request.query_params.get('id')):
            try:
                ingredients.objects.get(id=request.query_params.get('id')).delete()
            except:
                return (Response({"Error While Deleting"},status=status.HTTP_204_NO_CONTENT))
        else:
            return (Response({"Invalid Id"}, status=status.HTTP_204_NO_CONTENT))
        return (Response({"Message":"Deleted"},status=status.HTTP_200_OK))


# ________________________________Customer_Views______________________________________________________________________

class market(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        id="id"
        products_="products"
        if id in request.query_params:
            try:
                if(product.objects.filter(id=request.query_params[id]).exists()):
                    productU=product.objects.get(id=request.query_params[id])
                    result=Market(productU)
                else:
                    return (Response({"Invalid Id"}, status=status.HTTP_400_BAD_REQUEST))
            except:
                return (Response({"Invalid Id"}, status=status.HTTP_400_BAD_REQUEST))
        else:
            temp=product.objects.all()
            result=Market(temp,many=True)
        return (Response({products_:result.data},status=status.HTTP_200_OK))

    def sold(self,i,request):
        productN = "product"
        freq = "amount"
        product_ = product.objects.get(id=i[productN])
        recipes=recipe.objects.filter(product=product_)
        for j in recipes:
            j.ingredient.quantity=j.buy(i[freq])
            j.ingredient.save()
            # print(j)
        if(order_history.objects.filter(user=request.user).exists()):
            temp=order_history.objects.get(user=request.user)
        else:
            temp=order_history.objects.create(user=request.user)
        temp2=orders.objects.create(productKey=product_,freq=i[freq],order_id=temp)
        return OrderSer(temp2)
        # except:
        #     print(f"Invalid ID: {i[productN]}")
        #     return ({"amount":"invalid"})

    def post(self,request):
        cart="cart"
        resulCart=list()
        total=0
        if cart in request.data:
            arr=request.data[cart]
            for i in arr:
                    data=self.sold(i,request)
                    resulCart.append(data.data)
                    print(data.data)
                    total+=data.data['amount']
            return (Response({"data":resulCart,"Total":total}, status=status.HTTP_200_OK))
        else:
            return (Response({"Invalid Cart Entry"}, status=status.HTTP_400_BAD_REQUEST))

class OrderHistory(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        user=request.user
        order_=order_history.objects.get(user=user)
        temp=OrderSer(orders.objects.filter(order_id=order_),many=True)
        return Response({"data":temp.data},status=status.HTTP_200_OK)