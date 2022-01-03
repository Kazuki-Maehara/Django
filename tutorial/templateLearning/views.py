from django.shortcuts import render


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
