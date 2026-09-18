from django.shortcuts import render,redirect
from Movieapp.models import DataDB

# Create your views here.

def Function(request):
    return render(request,"Home.html")

def save_data(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        place=request.POST.get("place")
        object = DataDB(name=name, age=age, place=place)
        object.save()

    return redirect("Function")

def display(request):
    data = DataDB.objects.all()
    return render(request,"display.html",{'data':data})