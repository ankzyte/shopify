"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('register/',userViews.register,name='user-register'),
    path('user/',include('user.urls')),  
    path('login/',authViews.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',authViews.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    path('resetpassword/',userViews.sendEmail,name='user-email'),
    path('resetpassword/<int:user_id>/<str:token>/',userViews.passwordReset,name='user-resetpass')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)