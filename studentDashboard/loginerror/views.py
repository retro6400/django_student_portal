from django.shortcuts import render

def error_method(request):
    return render (request,'loginerror.html')
