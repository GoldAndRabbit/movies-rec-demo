from django.http import HttpResponse
from django.shortcuts import render


def user_view(request):
    context = {}
    names   = ['内容1', '内容2', '内容3', '内容4', '内容5', '内容6']
    data    = [1, 2, 3, 4, 5, 6]
    context['names']        = names
    context['data']         = data
    context['penetration']  = '低'
    context['recent']       = '低'
    context['amount']       = '低'
    context['cost']         = '低'
    if request.GET:
        context['penetration']  = request.GET['penetration']
        context['recent']       = request.GET['recent']
        context['amount']       = request.GET['amount']
        context['cost']         = request.GET['cost']
    return render(request, 'user.html', context)
