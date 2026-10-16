from django.http import HttpResponse
from django.shortcuts import render, reverse

def page(request):
    template_name = 'page.html'
    # впишите правильные адреса страниц, используя
    # функцию reverse
    pages = {
        'Главная страница': reverse('home'),
        'График Биткоина': reverse("page1"),
        # 'Показать содержимое рабочей директории': reverse("time")
        'Индекс страха и жадности': reverse("page2"),
        'Сигналы по стратегии EMA': reverse("page3")
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

