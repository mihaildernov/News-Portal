from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['is_not_sport_subscribers'] = not self.request.user.groups.filter(name='sport_subscribers').exists()
        context['is_not_business_subscribers'] = not self.request.user.groups.filter(name='business_subscribers').exists()
        context['is_not_education_subscribers'] = not self.request.user.groups.filter(name='education_subscribers').exists()
        context['is_not_entertainment_subscribers'] = not self.request.user.groups.filter(name='entertainment_subscribers').exists()
        return context