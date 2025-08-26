from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from .models import Tasks, Category
from django.urls import reverse_lazy
from .forms import TaskForm

class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        search_query = self.request.GET.get('q')

        if category_id:
            queryset = queryset.filter(category__id=category_id)
        
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset.order_by('title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')