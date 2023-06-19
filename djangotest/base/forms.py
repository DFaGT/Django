from django import forms
from .models import Parent
from .models import Student

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'postal_code', 'address', 'email', 'phone_number', 'terms', 'how_to_know']  # すべてのフィールドを使用する場合
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

        # 特定のフィールドのみ使用する場合は以下のように指定します
        # fields = ['name', 'postal_code', 'address', 'email', 'phone_number', 'status', 'terms', 'how_to_know']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'name_kana', 'birthday', 'gender', 'sibling', 'school', 'grade', 'phone_number', 'introducer', 'course']