from django.shortcuts import render

# Create your views here.
def learn_python(request):
    return render(request,"courses/coursepy.html")


def learn_django(request):
    return render(request,"courses/coursedj.html")