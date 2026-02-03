from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        # Assign the logged-in user to the task
        todo = Todo(user=request.user, title=title, desc=desc)
        todo.save()
        return redirect('list')
    return render(request, 'add_todo.html')

@login_required
def list(request):
    # Only get tasks belonging to the current user
    todo = Todo.objects.filter(user=request.user) 
    return render(request, 'list.html', {'todo': todo})

@login_required
def update(request, pk):
    # Ensure the task exists AND belongs to the user
    try:
        todo = Todo.objects.get(pk=pk, user=request.user)
    except Todo.DoesNotExist:
        return HttpResponse("You are not authorized to edit this task", status=403)
    if todo.complete:
        return redirect('list')
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.desc = request.POST.get('desc')
        # Handle the 'complete' status from a checkbox
        todo.complete = 'complete' in request.POST 
        todo.save()
        return redirect('list')
    return render(request, 'add_todo.html', {'todo': todo})

@login_required
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('list'))
    return render(request, 'delete.html', {'todo': todo})


from rest_framework import viewsets
from .serializers import TodoSerializer

@login_required
def complete_todo(request, pk):
    todo = Todo.objects.get(pk=pk, user=request.user) # Security: ensure it's their todo
    todo.complete = not todo.complete  # Toggles True to False, or False to True
    todo.save()
    return redirect('list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

        


