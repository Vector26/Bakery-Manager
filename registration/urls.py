from django.urls import path,include
from .views import *
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('adminSignup',adminSignup.as_view(),name="adminSignUp"),
    path('Signup',Signup.as_view(),name="signUp"),
]