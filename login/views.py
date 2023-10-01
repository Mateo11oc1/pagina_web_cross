from django.shortcuts import render
from .forms import MyUserCreationForm
from django.http import HttpResponse
from .models import User
from register.models import Country
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
        return render(request, 'login/create_account.html', context)
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            #Aqui las acciones si los datos son correctos
            country = Country(code='500', name='Chile')
            country.save()
            dni = request.POST['dni']
            username = request.POST['username']
            first_name = request.POST['first_name']
            email = request.POST['email']
            gender = request.POST['gender']
            password = request.POST.get('password1')
            user = User(dni=dni, username=username, first_name=first_name, email=email, gender=gender, country=country)
            user.set_password(password)
            user.save()
            return HttpResponse(request.POST['first_name'])
            
        else:
            #Aqui las acciones si los datos son incorrectos
            context = {'user_creation_form':form}
            return render(request, 'login/create_account.html', context)
    
    
