from django.http import HttpResponse
from django.shortcuts import render


def crowd_view(request):
    context = {}
    names = ['内容1', '内容2', '内容3', '内容4', '内容5', '内容6']
    data = [1, 2, 3, 4, 5, 6]
    context['names'] = names
    context['data']  = data
    return render(request, 'crowd.html', context)

