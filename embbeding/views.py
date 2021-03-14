from django.http import HttpResponse
from django.shortcuts import render


def test_embedding_view(request):
    return HttpResponse("embedding everything!")


def embedding_view(request):
    context = {}
    context['hello'] = 'embedding is cool'
    return render(request, 'embedding.html', context)
