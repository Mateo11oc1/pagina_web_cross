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

def goal(request):

    if request.method == 'GET':
        form = MyUserCreationForm()
        context = {'user_creation_form':form}
        return render(request, 'login/forms/create_account.html', context)

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            try:
                #Aqui las acciones si los datos son correctos
                dni = request.POST['dni']
                username = request.POST['username']
                first_name = request.POST['first_name']
                email = request.POST['email']
                gender = Gender.objects.get(id=request.POST['gender'])
                country = Country.objects.get(code=request.POST['country'])
                password = request.POST.get('password1')
                user = User(dni=dni, username=username, first_name=first_name, email=email, gender=gender, country=country)
                user.set_password(password)
                user.save()
                return render(request, 'login/index.html', {'user_creation_confirmation': 'Usuario creado exitosamente'})
            except IntegrityError as e:
                print(e)
                unicity_error_detail = str(e).capitalize()
                return render(request, 'login/create_account.html', {'unicity_error_detail': unicity_error_detail ,'user_creation_form': form})

        else:
            #Aqui las acciones si los datos son incorrectos
            return render(request, 'login/create_account.html', {'unicity_error': '', 'user_creation_form': form})


