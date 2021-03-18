from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'template_view_schoolapp/home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='seetma'
        context['rollno']=101
        return context


