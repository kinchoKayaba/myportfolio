from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Profile, Project, Skill, Education, Experience

# Create your views here.

class HomeView(TemplateView):
    """トップページのビュー"""
    template_name = 'portfolio_app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all().order_by('-created_at')[:3]  # 最新3件
        return context

class AboutView(TemplateView):
    """自己紹介ページのビュー"""
    template_name = 'portfolio_app/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['skills'] = Skill.objects.all()
        context['educations'] = Education.objects.all().order_by('-start_date')
        context['experiences'] = Experience.objects.all().order_by('-start_date')
        return context

class ProjectListView(ListView):
    """プロジェクト一覧ページのビュー"""
    model = Project
    template_name = 'portfolio_app/project_list.html'
    context_object_name = 'projects'
    ordering = ['-created_at']

class ProjectDetailView(DetailView):
    """プロジェクト詳細ページのビュー"""
    model = Project
    template_name = 'portfolio_app/project_detail.html'
    context_object_name = 'project'

class SkillListView(ListView):
    """スキル一覧ページのビュー"""
    model = Skill
    template_name = 'portfolio_app/skill_list.html'
    context_object_name = 'skills'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # カテゴリーごとにスキルをグループ化
        skills_by_category = {}
        for skill in self.get_queryset():
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)
        context['skills_by_category'] = skills_by_category
        return context
