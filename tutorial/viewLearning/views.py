from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

def myView_functionBased(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('Result for GET method on function-based  call')


class MyView_classBased(View):
    def get(self, request):
        return HttpResponse('Result for GET method on class-based call')


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


# A class for overridding the class GreetingView
class MorningGreetingView(GreetingView):
    greeting = "morning to ya"
