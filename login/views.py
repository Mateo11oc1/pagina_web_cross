from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/index.html', {})

def new_account(request):
    return render(request, 'login/create_account.html', {})
