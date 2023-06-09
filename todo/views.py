from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def task(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/task')
    task = Todo.objects.all().order_by('complete')
    return render(request,'todo/index.html',{'form':form,'tasks':task})



def delete(request,id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('/app/task')

def edit(request,id):
    task = Todo.objects.get(id=id)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/app/task')
        
    return render(request,'todo/edit.html',{'form':form})



def complete(request,id):
    task = Todo.objects.get(id=id)
    task.complete = True
    task.save()
    return redirect('/app/task')