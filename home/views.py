from django.shortcuts import render

def home(request):
    context = {}
    context['title'] = 'embedding is cool'
    return render(request, 'home.html', context)
