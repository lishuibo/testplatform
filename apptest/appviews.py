from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apptest.models import Appcase, Appcasestep
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
@login_required
def appcase_manage(request):
    appcase_list = Appcase.objects.all().order_by('id')
    username = request.session.get('user', '')
    paginator = Paginator(appcase_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        appcase_list = paginator.page(page)
    except PageNotAnInteger:
        appcase_list = paginator.page(1)
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)
    appcase_count = Appcase.objects.all().count()
    return render(request, 'appcase_manage.html',
                  {'user': username, 'appcases': appcase_list, 'appcasecounts': appcase_count})


@login_required
def appcasestep_manage(request):
    appcasestep_list = Appcasestep.objects.all()
    username = request.session.get('user', '')
    appcaseid = request.GET.get('appcase.id', None)
    appcase = Appcase.objects.get(id=appcaseid)
    return render(request, 'appcasestep_manage.html',
                  {'user': username, 'appcase': appcase, 'appcasesteps': appcasestep_list})


@login_required
def apptest_report(request):
    username = request.session.get('user', '')
    return render(request, 'apptest_report.html', {'user': username})


@login_required
def appsearch(request):
    username = request.session.get('user', '')
    search_appcasename = request.GET.get('appcasename', '')
    appcase_list = Appcase.objects.filter(appcasename__icontains=search_appcasename)
    return render(request, 'appcase_manage.html', {'user': username, 'appcases': appcase_list})


@login_required
def appstepsearch(request):
    username = request.session.get('user', '')
    search_appcasename = request.GET.get('appcasename', '')
    appcasestep_list = Appcasestep.objects.filter(appcasename__icontains=search_appcasename)
    return render(request, 'appcasestep_manage.html', {'user': username, 'appcasesteps': appcasestep_list})