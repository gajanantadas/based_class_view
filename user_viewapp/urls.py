from django.urls import path
from . import views
urlpatterns = [
    path('',views.UserAddShowView.as_view(),name='addandshow'),
    path('update<int:id>',views.UserUpdateView.as_view(),name='updatedata'),
    path('delete<int:id>',views.UserDeleteView.as_view(),name='deletedata'),
]