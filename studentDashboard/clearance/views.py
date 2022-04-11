from django.shortcuts import render

from clearance.models import clear

def clearance_method(request):
    data = clear.objects.all()
    return render (request,'clearance.html', {'clear': data})
