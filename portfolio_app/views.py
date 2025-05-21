from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Profile, Project, Skill, Education

# Create your views here.

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()[:3]  # 最新の3件を表示
    return render(request, 'portfolio_app/home.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    })

def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    educations = Education.objects.all().order_by('-start_date')
    return render(request, 'portfolio_app/about.html', {
        'profile': profile,
        'skills': skills,
        'educations': educations,
    })

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio_app/project_list.html', {
        'projects': projects,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio_app/project_detail.html', {
        'project': project,
    })

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
