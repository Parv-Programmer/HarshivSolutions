from django.contrib import admin
from .models import Product, Service, Contact

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']


# ============================================
# FILE: shop/views.py
# ============================================
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Service, Contact

def home(request):
    products = Product.objects.all()
    services = Service.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_text = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message_text
        )
        messages.success(request, 'Thank you! We will contact you soon.')
        return redirect('home')
    
    context = {
        'products': products,
        'services': services
    }
    return render(request, 'shop/home.html', context)