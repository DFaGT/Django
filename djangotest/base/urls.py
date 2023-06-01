from django.urls import path
from . import views

urlpatterns = [
    path('school/', views.SchoolListView.as_view(), name='school-list'),
    path('school/create/', views.SchoolCreateView.as_view(), name='school-create'),

]
