from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms.form_sample import NameForm,  ContactForm

# Create your views here.


def templateVariable_test(request):
    context = {'subject': 'Monkeys', 'food': 'banana'}
    return render(
        request,
        'templateLearning/templateVariable_test.html',
        context
    )


def csrfToken_test(request):
    context = {'text': 'CSRF token is below there.'}
    return render(
        request,
        'templateLearning/csrfToken_test.html',
        context
    )


def staticFile_test(request):
    return render(
        request,
        'templateLearning/staticFile_test.html',
    )


def form_test(request):
    # if this is a POST request we need to proces the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # chech whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # print(form.cleaned_data)
            # redirect to a new URL:
            return HttpResponseRedirect('/templateLearning/name_checked/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(
        request,
        'templateLearning/formLearning.html',
        {'form': form},
    )


def form_more_test(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            context = {
                'subject': subject,
                'message': message,
                'sender': sender,
                'cc_myself': cc_myself,
            }

            return render(
                request,
                'templateLearning/form_more_test_checked.html',
                context,
            )
    else:
        form = ContactForm()

    return render(
        request,
        'templateLearning/form_more_test.html',
        {'form': form},
    )


def name_checked(request):
    return render(
        request,
        'templateLearning/name_checked.html',
    )
