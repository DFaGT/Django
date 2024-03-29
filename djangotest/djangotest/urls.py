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
from studentMaster.views import SchoolListView, SchoolCreateView, StudentListView, ParentListView, StudentUpdateView, \
NewRegisterView, ParentUpdateView, SchoolEditView
from django.urls import path, include

app_name = 'studentMaster'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', SchoolListView.as_view(), name='school-list'),
    path('school/<int:pk>/edit/', SchoolEditView.as_view(), name='school_edit'),  # 編集ビューのURLパターンを追加

    path('student/', StudentListView.as_view(), name='student-list'),
    path('parent/', ParentListView.as_view(), name='parent-list'),
    path('school/create/', SchoolCreateView.as_view(), name='school-create'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('studentMaster/', include(('studentMaster.urls', 'studentMaster'), namespace='studentMaster')),
    path('new_register/', NewRegisterView.as_view(), name='new_register'),
    path('parent/<int:pk>/edit/', ParentUpdateView.as_view(), name='parent_edit'),

  # アプリ内のurls.pyをインクルード

]
