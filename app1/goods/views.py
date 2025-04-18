from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request):
    goods = Products.objects.all()

    cotext = {
        'title':'HOME - catalog',
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', cotext)

def product(request):
    return render(request, 'goods/product.html')