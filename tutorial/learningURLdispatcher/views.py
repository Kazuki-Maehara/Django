from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import datetime

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


def original_test(request, year):
    context = {'x': 'test context'}
    print(year)
    return render(
        request,
        'learningURLdispatcher/original_test.html',
        context,
    )


def regex_test(request, pattern):
    context = {'x': 'test context'}
    print(pattern)
    return render(
        request,
        'learningURLdispatcher/regex_test.html',
        context,
    )


def current_datetime(request):
    now = datetime.datetime.now()
    html = """
<html>
    <body>
        It is now {now}.
    </body>
</html>
    """.format(now=now)

    return HttpResponse(html)


def notFound_test(request, string):
    if string == '404':
        return HttpResponseNotFound('<h1>Pange not found</h1>')
    else:
        return HttpResponse('<h1>Page, other than NOT_FOUND</h1>')
