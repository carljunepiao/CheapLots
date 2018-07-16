from django.shortcuts import render

# Create your views here.


def rent(request):
    context = locals()
    template = 'rent.html'
    return render(request, template, context)
