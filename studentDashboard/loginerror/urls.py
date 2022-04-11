from django.urls import path
from . import views

urlpatterns = [
    path('loginerror', views.error_method, name = 'loginerror')
]