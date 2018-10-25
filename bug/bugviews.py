from django.shortcuts import render
from bug.models import Bug
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def bug_manage(request):
    bug_list = Bug.objects.all()
    username = request.session.get('user', '')
    return render(request, 'bug_manage.html', {'user': username, 'bugs': bug_list})

@login_required
def bugsearch(request):
    username = request.session.get('user', '')
    search_bugname = request.GET.get('bugname', '')
    bug_list = Bug.objects.filter(bugname__icontains=search_bugname)
    return render(request, 'bug_manage.html', {'user': username, 'bugs': bug_list})