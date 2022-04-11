from django.shortcuts import render

def courses_method(request):
    return render(request, 'courses.html')
