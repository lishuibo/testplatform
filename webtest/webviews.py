from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webtest.models import Webcase, Webcasestep
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all().order_by('id')
    username = request.session.get('user', '')
    paginator = Paginator(webcase_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        webcase_list = paginator.page(page)
    except PageNotAnInteger:
        webcase_list = paginator.page(1)
    except EmptyPage:
        webcase_list = paginator.page(paginator.num_pages)
    webcase_count = Webcase.objects.all().count()
    return render(request, 'webcase_manage.html',
                  {'user': username, 'webcases': webcase_list, 'webcasecounts': webcase_count})


@login_required
def webcasestep_manage(request):
    webcasestep_list = Webcasestep.objects.all()
    username = request.session.get('user', '')
    webcaseid = request.GET.get('webcase.id', None)
    webcase = Webcase.objects.get(id=webcaseid)
    return render(request, 'webcasestep_manage.html',
                  {'user': username, 'webcase': webcase, 'webcasesteps': webcasestep_list})


@login_required
def websearch(request):
    username = request.session.get('user', '')
    search_webcasename = request.GET.get('webcasename', '')
    webcase_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request, 'webcase_manage.html', {'user': username, 'webcases': webcase_list})


@login_required
def webstepsearch(request):
    username = request.session.get('user', '')
    search_webcasename = request.GET.get('webcasename', '')
    webcasestep_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request, 'webcasestep_manage.html', {'user': username, 'webcasesteps': webcasestep_list})


@login_required
def webtest_report(request):
    username = request.session.get('user', '')
    return render(request, 'webtest_report.html', {'user': username})