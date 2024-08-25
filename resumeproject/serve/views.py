from django.shortcuts import render

# Create your views here.
def serve(request):
    return render(request,"serve/services.html")