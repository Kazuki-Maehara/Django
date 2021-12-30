from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'x': 'test context'}
    return render(
        request,
        'learningURLdispatcher/index.html',
        context
    )


def converter_test(request, number):
    context = {'x': 'test context'}
    print(number)
    return render(
        request,
        'learningURLdispatcher/converter_test.html',
        context,
    )
