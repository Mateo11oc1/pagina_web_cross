from django.shortcuts import render
from .forms import MyUserCreationForm
from django.http import HttpResponse
from .models import User
from register.models import Country, Gender
from django.db import IntegrityError
# Create your views here.
def login(request):
    return render(request, 'login/index.html', {})

def new_account(request):
    form = MyUserCreationForm()
    context = {'user_creation_form':form}
    return render(request, 'login/create_account.html', context)

def new_account_succesfull(request):

    if request.method == 'GET':
        form = MyUserCreationForm()
        context = {'user_creation_form':form}
        return render(request, 'login/forms/create_account.html', context)

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            dni = request.POST['dni']
            username = request.POST['username']
            first_name = request.POST['first_name']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST.get('password1')
            gender = Gender.objects.get(id=request.POST['gender'])
            country = Country.objects.get(code=request.POST['country'])
            user = User(dni=dni, username=username, first_name=first_name, email=email, gender=gender, country=country, phone=phone)
            user.set_password(password)
            user.save()
            return render(request, 'login/index.html', {'user_creation_confirmation': 'Usuario creado exitosamente'})
        else:
            #Aqui las acciones si los datos son incorrectos
            return render(request, 'login/create_account.html', {'user_creation_form': form})


