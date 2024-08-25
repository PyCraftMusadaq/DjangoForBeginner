from django.shortcuts import HttpResponse
class BrotherMiddleware:
    def __init__(self,get_response):
        print("One Time Initliazation of Brother Middlware....")
        self.get_response = get_response
    def __call__(self,request):
        print("Before Functions in Brother Middleware.")
        response = self.get_response(request)
        print("After Functions in Brother Middleware.")
        return response
    

class FatherMiddleware:
    def __init__(self,get_response):
        print("One Time Initliazation of Father Middlware....")
        self.get_response = get_response
    def __call__(self,request):
        print("Before Functions in Father Middleware.")
        response = self.get_response(request)
        print("After View Function Fahter Middleware ")
        return response
    
class MotherMiddleware:
    def __init__(self,get_response):
        print("One Time Initliazation of Mother Middlware....")
        self.get_response = get_response
    def __call__(self,request):
        print("Before Functions in Mother Middleware.")
        response = self.get_response(request)
        print("After Functions in Mother Middleware.")
        return response

class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response 
    def process_view(request,*args,**kwargs):
        #return HttpResponse("This is Before View") when this line executes it elimates the view functions end the process here
        return None # but in case of none it will move towards the view function 
    
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response 
    def process_exception(self,request,exception):
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        # it will work when there is exception in the webpage 
        return HttpResponse(f"There is something wrong with view function {msg}")
    
     
class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response 
    def process_template_response(self,request,response):
        print("Reponse Template Hit via Middleware")
        response.context_data['name'] = "Mam Attofa Shoukat"
        return response 
    