from django.shortcuts import render
from bug.models import Bug
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def bug_manage(request):
    bug_list = Bug.objects.all()
    username = request.session.get('user', '')
    return render(request, 'bug_manage.html', {'user': username, 'bugs': bug_list})