from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('skills/', views.SkillListView.as_view(), name='skill_list'),
] 