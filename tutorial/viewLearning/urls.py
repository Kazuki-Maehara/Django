from django.urls import path
from . import views
from .views import MyView_classBased, GreetingView, MorningGreetingView

urlpatterns = [
    path(
        'myView_functionBased/',
        views.myView_functionBased,
        name = 'myView_functionBased'
        ),
    path(
        'MyView_classBased/',
        MyView_classBased.as_view(),
        name = 'MyView_classBased'
        ),
    path(
        'GreetingView/',
        GreetingView.as_view(),
        name = 'GreetingView'
        ),
    # path(
    #     'MorningGreetingView/',
    #     MorningGreetingView.as_view(),
    #     name = 'MorningGreetingView'
    #     ),
    path(
        'MorningGreetingView/',
        MorningGreetingView.as_view(greeting="Ha, it's overridden, good night"),
        name = 'MorningGreetingView'
        ),

]
