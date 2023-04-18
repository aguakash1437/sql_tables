from django.shortcuts import render

# Create your views here.
from app.models import *
def Dept(request):
    LOD=department.objects.all()
    d={'depts':LOD}
    return render(request,'Dept.html',d)

def Emp(request):
    LOE=Employee.objects.all()
    d={'emps':LOE}
    return render(request,'Emp.html',d)