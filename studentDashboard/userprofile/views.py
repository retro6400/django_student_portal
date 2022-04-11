from django.shortcuts import render

from userprofile.models import userinfo

def profile_method(request):
   uinfo = userinfo.objects.all()
   return render (request,'userprofile.html', {'userinfo': uinfo})




