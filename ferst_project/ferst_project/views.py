from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
    a=5
    return render(request, 'first_page.html', {'переменная':a})
