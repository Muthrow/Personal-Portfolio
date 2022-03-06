from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def howdy(request):
    return render(request, 'hello.html',{'name':'Taite'})