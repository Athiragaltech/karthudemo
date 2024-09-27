
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from . models import Employee
from django.shortcuts import render, get_object_or_404, redirect



def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})
    return render(request, 'index.html', context)
def addnew(request):
    return render(request,'addnew.html') 
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        desig=request.POST.get('desig')
        country=request.POST.get('country')
        mobile=request.POST.get('mobile')
        query=employee(name=name,age=age,place=place,desig=desig,country=country,mobile=mobile)
        query.save()
        return HttpResponse(f'<script>alert("File Saved successfully!"); window.location.href = "/";</script>')
    return render(request,'index.html') 
def view(request):
    data={
        'emp' :employee.objects.all()
         }
    return render(request,'view.html',data)
def edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    context = {'employee': employee}
    return render(request, 'edit.html', context)





   







def delete(request,id):
    dlt=employee.objects.get(id=id)
    dlt.delete()
    return HttpResponse(f'<script>alert("File Deleted successfully!"); window.location.href = "/";</script>')
         
    return render(request, 'index.html')


