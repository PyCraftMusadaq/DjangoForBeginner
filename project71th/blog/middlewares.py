# class based views 
from django.http import HttpResponse 

class BrotherMiddleware:
    def __init__(self, get_reponse):
        self.get_response = get_reponse
        print("One Time Initliazation of Brother Middlware...")

    def __call__(self,request):
        print('Before View Brother Middlware...')
        response = self.get_response(request)
        print("After View Brother Middlware...")
        return response 
        
class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time init of Father")

    def __call__(self,request):
        print("Before View Father Middleware")
       # response = self.get_response(request)  # This will render towards next view or middleware
        # what if we want to restrict the access to this point only then
        response = HttpResponse("Access Denied") 
        print("After view Father Middlware")
        return response
    
class MotherMiddleware:
    def __init__(self,get_response):
        print("One Time Initialzation of Mothe Middleware..")
        self.get_response = get_response

    def __call__(self,request):
        print("Before View Mother Middlware..")
        response = self.get_response(request)
        print("After view Mother Middlware")
        return response 
    