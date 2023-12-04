from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from .forms import TaskForm


class CustomLoginView(LoginView):
    template_name = 'TodoApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class CustomRegisterView(CreateView):
    template_name = 'TodoApp/Register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context


class TaskDetailView(DetailView):
    model = Task


class TaskFormMixin(LoginRequiredMixin):
    form_class = TaskForm
    template_name = 'TodoApp/create.html'
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user

        try:
            # Try to save the form
            return super().form_valid(form)
        except ValidationError as e:
            # Catch ValidationError and add an error to the form
            form.add_error(None, _(str(e)))
            return self.form_invalid(form)


class TaskCreateView(TaskFormMixin, CreateView):
    pass


class UpdateList(TaskFormMixin, UpdateView):
    pass


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'TodoApp/delete.html'
    success_url = reverse_lazy("tasks")
