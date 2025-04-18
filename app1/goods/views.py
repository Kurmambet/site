from django.shortcuts import render


def catalog(request):
    cotext = {
        'title':'HOME - catalog',
        # 'goods': goods,
    }

    return render(request, 'goods/catalog.html', cotext)

def product(request):
    return render(request, 'goods/product.html')