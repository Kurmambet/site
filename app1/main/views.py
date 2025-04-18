from goods.models import Categories
from django.shortcuts import render



def index(request):
    categories = Categories.objects.all()
    context = {
        'title' : 'Home - главная',
        'content' : 'Главная страница сайта',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'HOME - about',
        'content' : 'Страница о нас',
        'text_on_page': 'some pafos text'

    }
    return render(request, 'main/about.html', context)