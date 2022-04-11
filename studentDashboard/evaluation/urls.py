from django.urls import path
from . import views

urlpatterns = [
    path('evaluation', views.eva_method, name = 'evaluation')
]