from django.urls import path
from . import views

urlpatterns = [
    path('clearance', views.clearance_method, name = 'clearance')
]