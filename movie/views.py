from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Movie Review Home</h1>')
    #return render (request, 'home.html')
    return render (request, 'home.html', {'name': 'Kevin Quiroz'})

def about(request):
      #return HttpResponse('<h1>Movie Review About</h1>')
      return render (request, 'about.html')
