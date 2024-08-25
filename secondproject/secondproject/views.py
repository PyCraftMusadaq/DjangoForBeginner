from django.http import HttpResponse

def index(request):
    return HttpResponse("You are in Main Module of Project")