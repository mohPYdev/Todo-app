from django.forms import ModelForm , TextInput
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "description"})
        self.fields['title'].widget.attrs.update({'class': 'form-control' ,'placeholder': "title"})
        # self.fields['user'].widget.attrs.update({'class': 'form-control'})
        # self.fields['status'].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Task
        fields = '__all__' 
        exclude = ['status' , 'user']


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "Username"})
        self.fields['password1'].widget.attrs.update({'class': 'input100' ,'placeholder': "password"})
        self.fields['password2'].widget.attrs.update({'class': 'input100' , 'placeholder':"confirm password"})

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ] 