from django.http import HttpResponse


def index(request):
    return HttpResponse("hello")


def about(request):
    return HttpResponse("i am a good student")
