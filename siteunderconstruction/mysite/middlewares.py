from django.shortcuts import render
class SiteUnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print("Call From Middleware...")
        response = render(request,"mysite/temp.html")
        return response
     