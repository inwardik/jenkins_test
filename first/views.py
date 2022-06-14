from django.http import HttpResponse


def index(request):
    return HttpResponse("Fun. Release N2.")
