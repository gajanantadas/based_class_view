from django.urls import path
from template_view_schoolapp import views
urlpatterns = [
    path('',views.HomeTemplateView.as_view(extra_context={'course':'python'}),name='home'),
    path('home/<int:cl>',views.HomeTemplateView.as_view(),name='cl'),
    ]