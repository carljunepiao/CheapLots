from django.shortcuts import render

# Create your views here.


def properties(request):
    context = locals()
    template = 'properties.html'
    return render(request, template, context)
