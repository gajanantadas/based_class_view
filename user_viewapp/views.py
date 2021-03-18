from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
# Create your views here.
from .models import User
class UserAddShowView(TemplateView):
    template_name = 'user_viewapp/addandshow.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stud':stud,'fm':fm}
        return context
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=ps)
            reg.save()
            return HttpResponseRedirect('/')
class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
class UserUpdateView(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'user_viewapp/update.html',{'fm':fm})
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
        #return render(request,'user_viewapp/update.html',{'fm':fm})