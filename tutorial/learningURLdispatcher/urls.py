from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(
        'converter_test/<int:number>/',
        views.converter_test,
        name='converter_test'
    ),
]
