from django.http import HttpResponse
from typing import Any


# class ExecutionflowMiddleware(object):
#     def __init__(self, get_response):
#         print("Constructor is executed")
#         self.get_response = get_response

#     def __call__(self, request):
#         print("Processing of the request")
#         response = self.get_response(request)
#         print("Post processing of the request")
#         return response
    

# class AppMaintainenceMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         return HttpResponse("<h1>currently Application is under maintaince.. Please try after 2 days")


# class ErrorMessageMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_exception(self, request,exception):
#         return HttpResponse(f'<h1>Currenlty we are facing some techinal problem, please try after some time<br>Raised exception: {exception.__class__.__name__}<br>The exception message:{exception}</h1>')
        


class FirstMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("This line printed by Middleware-1 before processing request")
        response = self.get_response(request)
        print("This line printed by Middleware-1 after processing request")
        return response


class SecondMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("This line printed by Middleware-2 before processing request")
        response = self.get_response(request)
        print("This line printed by Middleware-2 after processing request")
        return response
