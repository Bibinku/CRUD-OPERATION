from django.shortcuts import render

# Create your views here.

def Function(request):
    return render(request,"Home.html")