from django.urls import path
from . import views 

urlpatterns = [
path('index', views.index, name='index'),
path('login', views.login, name='login'),
path('dashboard', view.dashboard, name='dashboard'),
]
