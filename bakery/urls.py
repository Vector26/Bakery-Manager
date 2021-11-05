from django.urls import path,include
from .views import *
urlpatterns = [
    path('ingredients',inventoryIngred.as_view(),name="inventoryIng"),
    path('products',inventoryRecipe.as_view(),name="inventoryRec"),
    path('order_history',OrderHistory.as_view(),name="orderHistory"),
    path('',market.as_view(),name="Market"),
]