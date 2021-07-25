from django.http import HttpResponse
from django.shortcuts import render


def about_view(request):
    context = {}
    names = ['内容1', '内容2', '内容3', '内容4', '内容5', '内容6']
    data = [1, 2, 3, 4, 5, 6]
    cols = ['c罗', '梅西', '卡卡', '小罗', '哈维', '小白']
    data2 = [6, 5, 4, 3, 2, 1]
    context['names'] = names
    context['data']  = data
    context['cols']  = cols
    context['data2']  = data2
    return render(request, 'about.html', context)

