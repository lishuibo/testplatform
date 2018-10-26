from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from set.models import Set
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
@login_required
def set_manage(request):
    set_list = Set.objects.all().order_by('id')
    username = request.session.get('user', '')
    paginator = Paginator(set_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        set_list = paginator.page(page)
    except PageNotAnInteger:
        set_list = paginator.page(1)
    except EmptyPage:
        set_list = paginator.page(paginator.num_pages)
    set_count = Set.objects.all().count()
    return render(request, 'set_manage.html', {'user': username, 'sets': set_list, 'setcounts': set_count})


@login_required
def set_user(request):
    user_list = User.objects.all().order_by('id')
    username = request.session.get('user', '')
    paginator = Paginator(user_list, 5)
    page = request.GET.get('page', 1)
    currentpage = int(page)
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    user_count = User.objects.all().count()
    return render(request, 'set_user.html', {'user': username, 'users': user_list, 'usercounts': user_count})


@login_required
def setsearch(request):
    username = request.session.get('user', '')
    search_setname = request.GET.get('setname', '')
    set_list = Set.objects.filter(setname__icontains=search_setname)
    return render(request, 'set_manage.html', {'user': username, 'sets': set_list})


@login_required
def usersearch(request):
    username = request.session.get('user', '')
    search_username = request.GET.get('username', '')
    user_list = User.objects.filter(username__icontains=search_username)
    return render(request, 'set_user.html', {'user': username, 'users': user_list})