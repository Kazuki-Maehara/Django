from django.shortcuts import render


# Create your views here.
def templateVariable_test(request):
    context = {'subject': 'Monkeys', 'food': 'banana'}
    return render(
        request,
        'templateLearning/templateVariable_test.html',
        context
    )
