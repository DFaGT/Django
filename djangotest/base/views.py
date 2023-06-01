# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import School

class SchoolListView(ListView):
    model = School
    template_name = 'school_list.html'
    context_object_name = 'schools'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_checked = self.request.GET.get('filter')
        if filter_checked == 'on':
            queryset = queryset.filter(classification='J')  # 中学校のみ絞り込み
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