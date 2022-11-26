from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import task

# Create your views here.

class NewTaskView(CreateView):
    model = task
    fields = '__all__'
    template_name = "todo/task_form.html"

class ListTaskView(ListView):
    model = task
    context_object_name = 'todo'

class DeleteTaskView(DeleteView):
    model = task
    success_url = '/todo/view'

class UpdateTaskView(UpdateView):
    model = task
    fields = '__all__'
    success_url = '/todo/view'

class DetailTaskView(DetailView):
    model = task
    fields = '__all__'
    success_url = '/todo/view'

