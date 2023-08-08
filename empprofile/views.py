from django.shortcuts import render
from .models import Employee
# Create your views here.

def home(request):
    employees=Employee.objects.all()
    return render(request,"empprofile/index.html",{'employees':employees})

def empdetail(request,pk):
    emp=Employee.objects.get(id=pk)
    return render(request,"empprofile/empdetails.html",{'emp':emp})