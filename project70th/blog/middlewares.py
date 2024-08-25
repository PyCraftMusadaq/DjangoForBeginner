import logging 
logger = logging.getLogger(__name__)

# def my_middleware(get_response):
#     # one time init..
#     print("One Time Initliazation...")
#     def my_function(request):
#         print("before view...")
#         response = get_response(request)
#         print("After view..")
#         return response 
#     return my_function


# class Based Middleware
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Initialization..")
        logger.info("One Time initialization")
       # write your Code here that will get only one time execution
    def __call__(self, request):
        # This is Before View 
        print("Before View..")
        logger.info("Before View Method")
        response = self.get_response(request)
        print("After View...")
        logger.info("After View Method")
        return response 