from django.shortcuts import render

from django.http import HttpResponse

def dhoni(request):
    return render(request,'dhoni.html')


def rayudu(request):
    return HttpResponse('<h1> rayuduuuuuuu</h1>')
