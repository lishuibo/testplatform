from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apptest.models import Appcase, Appcasestep
# Create your views here.
@login_required
def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    username = request.session.get('user', '')
    return render(request, 'appcase_manage.html', {'user': username, 'appcases': appcase_list})


@login_required
def appcasestep_manage(request):
    appcasestep_list = Appcasestep.objects.all()
    username = request.session.get('user', '')
    return render(request, 'appcasestep_manage.html', {'user': username, 'appcasesteps': appcasestep_list})
