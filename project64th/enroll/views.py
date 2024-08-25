from django.shortcuts import render
from django.core.cache import cache 
# Create your views here.
# single value cache
# def home(request):
#     # mv = cache.get('movie','has_expired')
#     # if mv == 'has_expired':
#     #     cache.set('movie','Pakistan Zindabad',timeout=10)
#     #     mv = cache.get('movie')
#     mv = cache.get_or_set('Fee',1000,timeout=30,version=2) 

#     return render(request,"enroll/home.html",context={'fm':mv})

# multiple values cache 
# def home(request):
#     data = {'name':'Attofa', 'roll':4}
#     cache.set_many(data,timeout=10)
#     sv = cache.get_many(data)

#     return render(request,"enroll/home.html",context={"stu":sv})

# deleting the cache 

# def home(request):
#     cache.delete('Fee', version=2)
#     return render(request,"enroll/home.html")

# def home(request):
#     cache.set('roll',100,timeout=600,version=10)
#     rv = cache.incr('roll', delta=1,version=10)
#     print(rv)

def home(request):
    cache.clear()
    return render(request,"enroll/home.html")


def contact(request):
    return render(request,"enroll/contact.html")