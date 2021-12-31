from django.urls import path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'converter_test/<yyyy:year>/',
        views.converter_test,
        name='converter_test'
    ),
]
