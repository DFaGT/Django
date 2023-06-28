from django import forms
from .models import Parent
from .models import Student
from .models import School

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['last_name','first_name', 'postal_code', 'address', 'email', 'phone_number', 'terms', 'how_to_know']  # すべてのフィールドを使用する場合
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

        # 特定のフィールドのみ使用する場合は以下のように指定します
        # fields = ['name', 'postal_code', 'address', 'email', 'phone_number', 'status', 'terms', 'how_to_know']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['last_name','first_name', 'last_name_kana', 'first_name_kana', 'birthday', 'gender', 'sibling', 'school', 'grade', 'phone_number', 'introducer', 'course', 'parent', 'status']  # すべてのフィールドを使用する場合



class SchoolForm(forms.ModelForm):
    exam_01 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
    exam_02 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
    exam_03 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
    exam_04 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
    exam_05 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))

    class Meta:
        model = School
        fields = ['name', 'classification', 'city', 'exam_01', 'exam_02', 'exam_03', 'exam_04', 'exam_05']


# from django import forms

# class SchoolForm(forms.ModelForm):
#     exam_01 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
#     exam_02 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
#     exam_03 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
#     exam_04 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))
#     exam_05 = forms.DateField(widget=forms.SelectDateWidget(attrs={'type': 'date'}))

#     class Meta:
#         model = School
#         fields = ['name', 'classification', 'city', 'exam_01', 'exam_02', 'exam_03', 'exam_04', 'exam_05']
