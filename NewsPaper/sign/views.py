from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me_authors(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

@login_required
def upgrade_me_sport(request):
    user = request.user
    sport_subscribers_group = Group.objects.get(name='sport_subscribers')
    if not request.user.groups.filter(name='sport_subscribers').exists():
        sport_subscribers_group.user_set.add(user)
    return redirect('/')

@login_required
def upgrade_me_business(request):
    user = request.user
    business_subscribers_group = Group.objects.get(name='business_subscribers')
    if not request.user.groups.filter(name='business_subscribers').exists():
        business_subscribers_group.user_set.add(user)
    return redirect('/')

@login_required
def upgrade_me_education(request):
    user = request.user
    education_subscribers_group = Group.objects.get(name='education_subscribers')
    if not request.user.groups.filter(name='education_subscribers').exists():
        education_subscribers_group.user_set.add(user)
    return redirect('/')

@login_required
def upgrade_me_entertainment(request):
    user = request.user
    entertainment_subscribers_group = Group.objects.get(name='entertainment_subscribers')
    if not request.user.groups.filter(name='entertainment_subscribers').exists():
        entertainment_subscribers_group.user_set.add(user)
    return redirect('/')
