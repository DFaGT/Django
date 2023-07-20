from django.urls import path
from . import views
from .views import register_student, StudentUpdateView, SchoolListView, StudentListView, NewRegisterView, ParentListView\
,ParentUpdateView
from . import views
from .views import register_view

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),  # トップページの追加
    path('school/', views.SchoolListView.as_view(), name='school-list'),
    path('school/create/', views.SchoolCreateView.as_view(), name='school-create'),
    path('register_parent/', views.register_parent, name='register_parent'),
    path('thanks/', views.thanks, name='thanks'),
    path('register_student/', register_student, name='register_student'),
    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('new_register/', NewRegisterView.as_view(), name='new_register'),
    path('parent/', ParentListView.as_view(), name='parent-list'),
    path('parent/<int:pk>/edit/', ParentUpdateView.as_view(), name='parent_edit'),
    path('add_register/', views.register_student, name='add_register'),
    path('search_parent/', views.search_parent, name='search_parent'),

]
