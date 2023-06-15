from django import forms
from .models import Parent

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'  # すべてのフィールドを使用する場合

        # 特定のフィールドのみ使用する場合は以下のように指定します
        # fields = ['name', 'postal_code', 'address', 'email', 'phone_number', 'status', 'terms', 'how_to_know']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'name_kana', 'birthday', 'gender', 'sibling', 'school', 'parent', 'grade', 'status', 'phone_number', 'introducer', 'course']