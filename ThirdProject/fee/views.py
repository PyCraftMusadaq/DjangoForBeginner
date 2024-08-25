from django.shortcuts import render

# Create your views here.
def fee_django(request):
    return render(request,'fees/feedj.html')

def fee_python(request):
    return render(request,"fees/feepy.html")


