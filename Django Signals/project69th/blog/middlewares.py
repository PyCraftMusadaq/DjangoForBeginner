def my_middleware(get_reponse):
    # code in this section only runs once for each request to the server....
    print("One Time Initliazation...")
    def my_function(request):
       # The code before get_response will be run before he running of the actual view
        print("The Code before View... ") 
        response = get_reponse(request)
        # Th code after the running of actual view or next middleware will be get executed here..
        print("The code after View..")
        return response 
    return my_function
