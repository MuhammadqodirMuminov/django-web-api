from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('function', views.hello_world, name='hello_world'),
    path('reservation', views.home, name='home'),
]