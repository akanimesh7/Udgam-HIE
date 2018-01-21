from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .forms import UserForm
# Create your views here.
# def home(request):
#     cart=Cart(request)
#     return render(request,'shop/Products/index.html',{'cart':cart})

def product_list(request,category_slug=None):
        category=None
        categories=Category.objects.all()
        product_results = Product.objects.all()
        query = request.GET.get("q")
        if query:
            categories = categories.filter(
                Q(name__icontains=query)
            ).distinct()
            product_results = product_results.filter(
                Q(name__icontains=query)
            ).distinct()
            return render(request, 'shop/Products/search.html', {
                'categories': categories,
                'products': product_results,
            })
        else:
            if category_slug:
                category=get_object_or_404(Category,slug=category_slug)
                product_results=product_results.filter(category=category)
        return render(request,'shop/Products/list.html',{'category':category,'categories':categories,'products':product_results})

def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    return render(request,'shop/Products/detail.html',{'product':product,'cart_product_form':cart_product_form})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'shop/Products/list.html')
    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)
