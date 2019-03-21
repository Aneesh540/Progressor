from django import forms
from .models import Directory,Todoentry,Details

class AddTodoentry(forms.Form):
    attrs = {'class': 'form-control',
             'placeholder': 'new todo entry ',
             'rows': '3',
             'type': 'text', }
    input_text = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs=attrs),
                                 label='')

class NewDirectoryForm(forms.ModelForm):
    class Meta:
        attrs = {'class': 'form-control',
                 'placeholder': 'New. Directory',
                 'rows': '3',
                 'type': 'text', }

        model = Directory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs=attrs)
        }

class AddTodo(forms.ModelForm):
    class Meta:
        model = Todoentry
        fields = ["entry"]
