from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import *
from tasks.models import *
# Create your views here.
def home(request):
	return render(request,'tasks/mainpage.html')

def index(request,fk):
	tasks=Task.objects.filter(uid=fk)
	form=TaskForm()
	if request.method =='POST':
		form=TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	context={'tasks':tasks,'form':form}
	return render(request,'tasks/list.html',context)

def update(request,pk):
	task=Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method=='POST':
		form=TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('index')
	context={'form':form}
	return render(request,'tasks/update_task.html',context)

def delete(request,pk):
	item=Task.objects.get(id=pk)
	if request.method=='POST':
		item.delete()
		return redirect('index')
		
	context={'item':item}
	return render(request,'tasks/delete_task.html',context)