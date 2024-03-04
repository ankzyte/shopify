from django.urls import path,include
from .views import ProductListView,ProductTypeListView,ProductDetailView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(),name="shop-home"),
    path('product/<str:type>/',ProductTypeListView.as_view(),name="shop-product"),
    path('<str:type>/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('<str:type>/<int:pk>/addtocart/',views.addToCart,name="addto-cart"),
    path('<str:type>/<int:pk>/checkcart/',views.checkCart,name="check-cart"),
]

