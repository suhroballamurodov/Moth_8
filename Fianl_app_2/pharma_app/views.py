from django.shortcuts import render



def index(request):
    return render(request,'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render (request, 'contact.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def shop_single(request):
    return render(request, 'shop-single.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})