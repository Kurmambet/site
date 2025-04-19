from django.shortcuts import render


def index(request):
    
    context = {
        'title' : 'Home - главная',
        'content' : 'Главная страница сайта',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'HOME - about',
        'content' : 'Страница о нас',
        'text_on_page': 'some pafos text'

    }
    return render(request, 'main/about.html', context)