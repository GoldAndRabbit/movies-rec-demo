from django.http import HttpResponse
from django.shortcuts import render


def i2i_view(request):
    context = {}
    movies_infos = {}
    for i in list(range(1, 32)):
        movies_infos[i] = {}
        movies_infos[i]['index']  = str(i)
        movies_infos[i]['pic']   = '/static/images/demo_pictures/' + str(i) + '.jpg'
        movies_infos[i]['intro']  = '这是第' + str(i) + '部电影, 讲述了一个非常动人的故事'
    context['movies'] = movies_infos
    return render(request, 'i2i.html', context)

