from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,"registration/profile.html")
# def userlogout(request):
#     return render(request,"registration/logged_out.html")