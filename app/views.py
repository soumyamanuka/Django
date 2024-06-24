from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    name = request.POST['name']
    email= request.POST['email']
    User = Data.objects.create(Name=name,Email=email)
    return render(request,"app/show.html")

def ShowPage(request):
    all_data=Data.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

def EditPage(request,pk):
    get_data=Data.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata=Data.objects.get(id=pk)
    udata.Name = request.POST['name']
    udata.Email = request.POST['email']
    udata.save()
    return redirect('showpage')

def DeleteData(request,pk):
    ddata = Data.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')
