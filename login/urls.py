from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('newaccount/', views.new_account, name="newaccount"),
    path('succesfullAccount/', views.new_account_succesfull, name='new_account_succesfull'),
]
