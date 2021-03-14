from django.http import HttpResponse


def i2i_view(request):
    return HttpResponse("i2i view!")