from django import forms
from studentapp.models import student
class add_student(forms.ModelForm):
    class Meta:
        model= student
        fields = '__all__'