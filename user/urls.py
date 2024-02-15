from django.urls import path,include
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [

    path('profile/',views.profile,name='user-profile'),
    path('address/',views.address,name='user-address'),

]