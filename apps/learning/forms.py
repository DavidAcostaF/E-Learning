from django import forms
from .models import ClassRoom,ClassPosts

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

class FormPost(forms.ModelForm):
    class Meta:
        model = ClassPosts
        fields = ['title','content']
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Classroom title'
                }),
            'content':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Classroom content'
                })
        }