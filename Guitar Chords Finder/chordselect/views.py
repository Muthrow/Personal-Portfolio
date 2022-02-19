from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def form(request):
    return render(request, 'form.html')

def form_output(request):
    return render(request, 'form_output.html')