# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import School
from .models import Student
from .models import Parent
from django.shortcuts import render
from .forms import ParentForm
from django.http import HttpResponse
from .forms import StudentForm
from django.urls import reverse_lazy


class SchoolListView(ListView):
    model = School
    template_name = 'school_list.html'
    context_object_name = 'schools'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_checked = self.request.GET.get('filter')
        if filter_checked == 'on':
            queryset = queryset.filter(classification='中学校')  # 中学校のみ絞り込み
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_checked'] = self.request.GET.get('filter')
        return context

class SchoolCreateView(CreateView):
    model = School
    template_name = 'base/school_create.html'
    fields = ['name', 'classification', 'city']
    success_url = '/school/'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_checked = self.request.GET.get('filter')
        if filter_checked == 'on':
            queryset = queryset.filter(status='A')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_checked'] = self.request.GET.get('filter')
        return context

class ParentListView(ListView):
    model = Parent
    template_name = 'parent_list.html'
    context_object_name = 'parents'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_checked = self.request.GET.get('filter')
        if filter_checked == 'on':
            queryset = queryset.filter(status='A')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_checked'] = self.request.GET.get('filter')
        return context
    

def register_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks') 
    else:
        form = ParentForm()

    return render(request, 'base/register_parent.html', {'form': form})

def thanks(request):
    return HttpResponse("Thank you for registering!")

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = StudentForm()

    return render(request, 'base/register_student.html', {'form': form})

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'base/student_update.html'
    success_url = reverse_lazy('student_list')