from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('newaccount/', views.new_account, name="new_account")
]
