# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import School
from .models import Student
from .models import Parent

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