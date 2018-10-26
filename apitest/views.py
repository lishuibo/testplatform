from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apitest.models import Apistep, Apitest, Apis
import pymysql
from .tasks import hello_world
from .tasks import apisauto_testcase, apitest_testcase
from .webtasks import webauto_testcase, webauto_testcase2
from .apptasks import appauto_testcase, appauto_testcase2
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule
# Create your views here.

def test(request):
    return HttpResponse("hello world")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def left(request):
    return render(request, 'left.html')


def welcome(request):
    return render(request, 'welcome.html')


@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all().order_by('id')
    username = request.session.get('user', '')
    paginator = Paginator(apitest_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        apitest_list = paginator.page(page)
    except PageNotAnInteger:
        apitest_list = paginator.page(1)
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages)
    apitest_count = Apitest.objects.all().count()
    return render(request, 'apitest_manage.html',
                  {'user': username, 'apitests': apitest_list, 'apitestcounts': apitest_count})


@login_required
def apistep_manage(request):
    apistep_list = Apistep.objects.all()
    username = request.session.get('user', '')
    apitestid = request.GET.get('apitest.id', None)
    apitest = Apitest.objects.get(id=apitestid)
    return render(request, 'apistep_manage.html', {'user': username, 'apitest': apitest, 'apisteps': apistep_list})


@login_required
def apis_manage(request):
    apis_list = Apis.objects.all().order_by('id')
    username = request.session.get('user', '')
    paginator = Paginator(apis_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        apis_list = paginator.page(page)
    except PageNotAnInteger:
        apis_list = paginator.page(1)
    except EmptyPage:
        apis_list = paginator.page(paginator.num_pages)
    apis_count = Apis.objects.all().count()
    return render(request, 'apis_manage.html', {'user': username, 'apiss': apis_list, 'apiscounts': apis_count})


@login_required
def test_report(request):
    apis_list = Apis.objects.all()
    username = request.session.get('user', '')
    apis_count = Apis.objects.all().count()
    db = pymysql.connect(user='root', db='autotest', passwd='123456', host='127.0.0.1')
    cursor = db.cursor()
    sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1;'
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0;'
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    return render(request, 'report.html',
                  {'user': username, 'apiss': apis_list, 'apiscounts': apis_count, 'apis_pass_counts': apis_pass_count,
                   'apis_fail_counts': apis_fail_count})


@login_required
def apitest_report(request):
    username = request.session.get('user', '')
    return render(request, 'apitest_report.html', {'user': username})


@login_required
def apisearch(request):
    username = request.session.get('user', '')
    search_apitestname = request.GET.get('apitestname', '')
    apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})


@login_required
def apissearch(request):
    username = request.session.get('user', '')
    search_apiname = request.GET.get('apiname', '')
    apis_list = Apis.objects.filter(apiname__icontains=search_apiname)
    return render(request, 'apis_manage.html', {'user': username, 'apiss': apis_list})


@login_required
def periodic_task(request):
    task_list = PeriodicTask.objects.all().order_by('id')
    periodic_list = IntervalSchedule.objects.all()
    crontab_list = CrontabSchedule.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(task_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        task_list = paginator.page(page)
    except PageNotAnInteger:
        task_list = paginator.page(1)
    except EmptyPage:
        task_list = paginator.page(paginator.num_pages)
    task_count = PeriodicTask.objects.all().count()
    return render(request, 'periodic_task.html',
                  {'user': username, 'tasks': task_list, 'taskcounts': task_count, 'periodics': periodic_list,
                   'crontabs': crontab_list})


@login_required
def tasksearch(request):
    username = request.session.get('user', '')
    search_taskname = request.GET.get('task', '')
    task_list = PeriodicTask.objects.filter(task__icontains=search_taskname)
    periodic_list = IntervalSchedule.objects.all()
    crontab_list = CrontabSchedule.objects.all()
    return render(request, 'periodic_task.html', {'user': username, 'tasks': task_list, 'periodics': periodic_list,
                                                  'crontabs': crontab_list})


def task_apis(request):
    apisauto_testcase.delay()
    return HttpResponse("run")


def task_apitest(request):
    apitest_testcase(request)
    return HttpResponse("run")


def task_webtest(request):
    webauto_testcase(request)
    return HttpResponse("run")


def task_webtest2(request):
    webauto_testcase2(request)
    return HttpResponse("run")


def task_apptest(request):
    appauto_testcase(request)
    return HttpResponse("run")


def task_apptest2(request):
    appauto_testcase2(request)
    return HttpResponse("run")

