from django.forms import ModelForm
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'dni', 'phone', 'gender', 'date_of_birth', 'height', 'weight']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user_creation_input',
                                            'id':'creation_username',
                                            'maxlength':150,
                                            }),
            'date_of_birth': forms.DateInput(attrs={'class':'user_creation_input',
                                                'id':'creation_dateofbirth',
                                                'type':'date',})
        }
    
    # Validación personalizada para las contraseñas
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
