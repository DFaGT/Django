from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("school-list/", views.SchoolView.as_view(), name="school-list"),
]
