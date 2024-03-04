from django.shortcuts import render
from .models import Product
from user.models import Cart
from django.views.generic import ListView,DetailView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    products = Product.objects.all()
    context={
        'title':'home',
        'products':products
    }
    return render(request,'shop/home.html',context)

class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

class ProductTypeListView(ListView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs['type']
        return context

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'products'

@login_required
def addToCart(request,**kwargs): 
    if request.user.is_authenticated:
        product_id = kwargs.get('pk')
        product = Product.objects.get(id=product_id)
        if Cart.objects.filter(user=request.user).exists():
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.create(user = request.user)    
        cart.products.add(product)
        return JsonResponse({'message': 'Cart created successfully'}, status=201)
    else:
        return JsonResponse({'message': 'User is not authenticated'}, status=401)

@login_required
def checkCart(request,**kwargs):
    if request.user.is_authenticated:
        product_id = kwargs.get('pk')
        product = Product.objects.get(id=product_id)
        if Cart.objects.filter(user=request.user).exists():
            cart = Cart.objects.get(user=request.user)
            if cart.products.filter(id=product_id).exists():
                return JsonResponse({'message': 'item exists'}, status=201)
    else:
        return JsonResponse({'message': 'User is not authenticated'}, status=401)

        
