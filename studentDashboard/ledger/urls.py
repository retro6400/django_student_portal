from django.urls import path
from . import views

urlpatterns = [
    path('ledger', views.ledger_method, name = 'ledger')
]