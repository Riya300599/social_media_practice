from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
]
