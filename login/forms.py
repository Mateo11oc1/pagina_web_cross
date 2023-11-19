from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class MyUserCreationForm(forms.Form):
    
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    username = forms.CharField(label='Nombre de usuario:', required=True, help_text='Ingrese un nombre de usuario', )
    first_name = forms.CharField(label='Nombre:', required=True)
    last_name = forms.CharField(label='Apellido:', required=False)
    email = forms.EmailField(label="Email:", required=True)
    dni = forms.CharField(label='Cédula de identidad:', min_length=10, max_length=10, required=True, widget=forms.TextInput(attrs={'type': 'text', 'pattern': '[0-9]*'}))
    phone = forms.CharField(label='Numero celular:',min_length=10, max_length=10, widget=forms.TextInput(attrs={'type': 'text', 'pattern':'[0-9]*'}))
    gender = forms.ChoiceField(label='Género:', choices=GENDER_CHOICES, widget=forms.Select, required=True)
    date_of_birth = forms.DateTimeField(label='Fecha de nacimiento:', widget=forms.SelectDateWidget())
    height = forms.IntegerField(label='Estatura:', help_text='Ingrese la estatura en centímetros.')
    weight = forms.IntegerField(label='Peso:', help_text='Ingrese su peso en kilogramos')
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Repita su contraseña',
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'dni', 'phone', 'gender', 'date_of_birth', 'height', 'weight']

    # Validación personalizada para las contraseñas
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
