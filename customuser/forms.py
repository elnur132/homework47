from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from .models import CreateUser


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=15, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2 = forms.CharField(max_length=15, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    
    class Meta:
        model = CreateUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'phone', 'avatar')
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
class AskForm(ModelForm):
    
    class Meta:
        model = CreateUser
        fields = ('age', 'text')