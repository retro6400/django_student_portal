from django.urls import path
from . import views

urlpatterns = [
    path('routine', views.routine_method, name = 'routine')
]