from django.urls import path
from . import views

urlpatterns = [
    path(
        'templateVariable/',
        views.templateVariable_test,
        name='templateVariable_test'
    ),
    path(
        'csrfToken_test/',
        views.csrfToken_test,
        name='csrfToken_test'
    ),
    path(
        'staticFile_test/',
        views.staticFile_test,
        name='staticFile_test'
    ),
    path(
        'form_test/',
        views.form_test,
        name='form_test'
    ),
    path(
        'form_more_test/',
        views.form_more_test,
        name='form_more_test'
    ),
    path(
        'name_checked/',
        views.name_checked,
        name='name_checked'
    ),
]
