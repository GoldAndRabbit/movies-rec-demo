from django.shortcuts import render

def home(request):
    context = {}
    for i in list(range(1, 30, 1)):
        context[i] = str(i) + '1.jpg'
    return render(request, 'home.html', context)
