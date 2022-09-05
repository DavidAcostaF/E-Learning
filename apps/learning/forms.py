from django import forms
from .models import ClassRoom

class FormClassRoom(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name','description']

        widgets = {
            'name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Classroom name'
                }
            ),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Classroom description'})}