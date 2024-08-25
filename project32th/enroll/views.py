from django.shortcuts import render, HttpResponseRedirect
from .forms import FormModel
from .models import User  
# Create your views here.
def add_show(request):
    
    if request.method=='POST':
        form = FormModel(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            reg = User(name=name,email=email,password=password)
            reg.save()
            form = FormModel()
            stud = User.objects.all()
            return render(request,"enroll/addandshow.html",{'form':form,'stu':stud})
    else:
        form = FormModel()
        stud = User.objects.all()
    return render(request,"enroll/addandshow.html",{'form':form,'stu':stud}) 


# delete function 
def delete_row(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        if pi:
            pi.delete() 
    return HttpResponseRedirect('/enroll/')


# edit the data 
def edit_row(request,id):
    if request.method=='POST':
        dt = User.objects.get(pk=id)
        form = FormModel(request.POST,instance=dt)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = FormModel(instance=pi) 
    return render(request,"enroll/updatedata.html",{'form':form})