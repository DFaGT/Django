from django.shortcuts import render
from .models import School
from django.views import View

class SchoolView(View):
    def get(self, request):
        template_name = "base/school-list.html"
        ctx = {}
        qs = School.objects.all()
        ctx["object_list"] = qs
        return render(request, template_name, ctx)