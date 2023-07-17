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
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "base/home.html"

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
    
def thanks(request):
    return HttpResponse("Thank you for registering!")

def register_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:thanks') 
    else:
        form = ParentForm()

    return render(request, 'base/register_parent.html', {'form': form})


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:thanks')
    else:
        form = StudentForm()

    return render(request, 'base/register_student.html', {'form': form})

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'base/student_update.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        print('Form is valid:', form.is_valid())
        response = super().form_valid(form)
        print('Response:', response)
        print('Redirecting to:', self.get_success_url())
        return response

    def form_invalid(self, form):
        print('Form is invalid:', form.is_valid())
        print('Form errors:', form.errors)
        return super().form_invalid(form)

from django.shortcuts import redirect
from django.views import View
from django.contrib.sessions.models import Session
from .forms import ParentForm, StudentForm


class NewRegisterView(View):
    def get(self, request):
        student_form = StudentForm(prefix='student')
        parent_form = ParentForm(prefix='parent')
        return render(request, 'base/new_register.html', {'student_form': student_form, 'parent_form': parent_form})

    def post(self, request):
        student_form = StudentForm(request.POST, prefix='student')
        parent_form = ParentForm(request.POST, prefix='parent')
        if student_form.is_valid() and parent_form.is_valid():
            parent = parent_form.save()  # 保護者を保存
            student = student_form.save(commit=False)
            student.parent = parent  # 生徒の parent フィールドに関連付ける
            student.save()
            return redirect('base:thanks')
        else:
            print('Student form errors:', student_form.errors)
            print('Parent form errors:', parent_form.errors)

        # エラーメッセージを追加
        student_form.add_error(None, '保護者情報が必要です。')

        return render(request, 'base/new_register.html', {'student_form': student_form, 'parent_form': parent_form})


    def save_form(self, form):
        # セッションから保護者情報を取得
        session_key = form.cleaned_data.get('session_key')
        try:
            session = Session.objects.get(session_key=session_key)
            parent_data = session.get_decoded()
            parent_form = ParentForm(parent_data, prefix='parent')
            if parent_form.is_valid():
                parent = parent_form.save()
                form.instance.parent = parent
            else:
                print('Parent form errors:', parent_form.errors)
        except Session.DoesNotExist:
            pass  # セッションが見つからない場合は何もしない

    def post(self, request):
        student_form = StudentForm(request.POST, prefix='student')
        parent_form = ParentForm(request.POST, prefix='parent')
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.session_key = request.session.session_key
            self.save_form(student_form)  # 保護者情報を関連付ける
            student.save()
            return redirect('base:thanks')
        else:
            print('Student form errors:', student_form.errors)

        return render(request, 'base/new_register.html', {'student_form': student_form, 'parent_form': parent_form})

register_view = NewRegisterView.as_view()
