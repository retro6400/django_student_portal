from django.shortcuts import render
from . models import dashinfo, graphres


def home_method(request):
   Dinfo = dashinfo.objects.all()
   Rinfo = graphres.objects.all()
   return render (request,'homepage.html', {'dashinfo': Dinfo, 'graphres': Rinfo})



