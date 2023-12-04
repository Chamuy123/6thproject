from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')


def faf(request):
    return HttpResponse('<h1>hiiii faf<h1>')
