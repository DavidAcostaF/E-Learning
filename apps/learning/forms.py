from dataclasses import field
from django import forms
from .models import ClassRoom,Posts,Files

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
            'description':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Classroom description'
                    })
            }

class FormPost(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if(kwargs.get('form_kwargs')):
            data = kwargs.pop('form_kwargs')
            self.user = data.pop('user')
            self.code = data.pop('code')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Posts
        fields = ['title','content','start_date','end_date','activity','files']
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Title...'
                }),
            'content':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Content...'
                }),
            'start_date':forms.DateInput(
                attrs={
                'class':'form-control',
                'type':'date'
            }),
            'end_date':forms.DateInput(
                attrs={
                'class':'form-control',
                'type':'date'
            }),
            'activity':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Activity...'
            }),
            'files':forms.FileInput(
            attrs={
                'class':'form-control',
                'multiple':'true'
            })
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        self.user
        
        if commit:
            instance.user = self.user
            instance.class_room = self.code
            instance.save()
        return instance


class FormSubmitFiles(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['files','comment']

        widgets = {
            'files':forms.FileInput(),
            'comme':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Add comment'
                }
            )
        }

class FromGradeAssingment(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['grade','comment']
        widgets = {
            'grade':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'comment':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),
        }