from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.SchoolListView.as_view(), name='school-list'),
    path('school/create/', views.SchoolCreateView.as_view(), name='school-create'),

]
