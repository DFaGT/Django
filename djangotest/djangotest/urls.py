"""
URL configuration for djangotest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import SchoolListView, SchoolCreateView, StudentListView, ParentListView, StudentUpdateView, \
NewRegisterView
from django.urls import path, include

app_name = 'base'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', SchoolListView.as_view(), name='school-list'),
    path('student/', StudentListView.as_view(), name='student-list'),
    path('parent/', ParentListView.as_view(), name='parent-list'),
    path('school/create/', SchoolCreateView.as_view(), name='school-create'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('base/', include(('base.urls', 'base'), namespace='base')),
    path('new_register/', NewRegisterView.as_view(), name='new_register'),
  # アプリ内のurls.pyをインクルード

]
