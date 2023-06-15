from django.urls import path
from . import views
from .views import register_student


urlpatterns = [
    path('school/', views.SchoolListView.as_view(), name='school-list'),
    path('school/create/', views.SchoolCreateView.as_view(), name='school-create'),
    path('register_parent/', views.register_parent, name='register_parent'),
    path('thanks/', views.thanks, name='thanks'),
    path('register_student/', register_student, name='register_student'),
]
