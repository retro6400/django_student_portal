from django.shortcuts import render

from login.models import active, logdata

def login_method(request):
    data = logdata.objects.all()
    ac = active.objects.all()
    return render (request,'login.html', {'logdata': data, 'active': ac})
