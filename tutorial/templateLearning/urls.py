from django.urls import path
from . import views

urlpatterns = [
    path(
        'templateVariable/',
        views.templateVariable_test,
        name='templateVariable_test'
    ),
]
