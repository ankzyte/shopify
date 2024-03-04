from django.urls import path,include
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [

    path('',views.createProfile,name='user-profile'),
    path('address/',views.address,name='user-address'),
    path('changepassword/',views.changePassword,name='user-changepass'),
    path('showcart/',views.showCart,name='user-cart')
]