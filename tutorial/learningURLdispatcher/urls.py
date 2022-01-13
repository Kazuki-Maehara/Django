from django.urls import re_path, path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'converter_test/<yyyy:year>/',
        views.original_test,
        name='original_test'
    ),
    path(
        'converter_test/<int:number>/',
        views.converter_test,
        name='converter_test'
    ),
    re_path(
        r'^regex_test/(?P<pattern>regex[0-9])/$',
        views.regex_test,
        name='regex_test'
    ),
    path(
        'current_datetime/',
        views.current_datetime,
        name='current_datetime'
    ),
    path(
        'notFound_test/<str:string>/',
        views.notFound_test,
        name='notFound_test'
    ),
]
