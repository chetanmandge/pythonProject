from django.shortcuts import render
from django.http import HttpResponse
from studentapp.forms import add_student
from studentapp.models import student
# Create your views here.
def welcome(request):
    return render(request,"studentapp/index.html")


def add_student_view(request):
    form=add_student()
    if request.method== 'POST':
        form=add_student(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"studentapp/add.html",{'form': form})
   
   
def list_student_view(request):
    data= student.objects.all()
    return render(request,'studentapp/list.html',{'data':data})