from django.shortcuts import render

# Create your views here.


def buy(request):
    context = locals()
    template = 'buy.html'
    return render(request, template, context)
