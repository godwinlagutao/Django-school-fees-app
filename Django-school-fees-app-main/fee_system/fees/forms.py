from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'department', 'level']
        
    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError("This student ID is already registered.")
        return student_id