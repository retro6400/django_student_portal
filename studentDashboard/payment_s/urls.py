from django.urls import path
from . import views

urlpatterns = [
    path('scheme', views.scheme_method, name = 'payment_s')
]