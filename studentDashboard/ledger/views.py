from django.shortcuts import render

from homepage.models import dashinfo
from userprofile.models import userinfo

def ledger_method(request):
    dinfo = dashinfo.objects.all()
    uinfo = userinfo.objects.all()
    return render (request, 'ledger.html', {'dashinfo': dinfo, 'userinfo': uinfo})
