import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio_app.models import Profile, Skill, Project, Education, Experience, Technology

# プロフィールの作成
profile = Profile.objects.create(
    name="山田 太郎",
    title="Python/Django開発者",
    bio="PythonとDjangoを使用したWebアプリケーション開発を専門としています。",
    github_url="https://github.com/example",
    linkedin_url="https://linkedin.com/in/example"
)

# スキルの作成
skills = [
    Skill.objects.create(name="Python", category="programming", level=5),
    Skill.objects.create(name="Django", category="framework", level=4),
    Skill.objects.create(name="HTML/CSS", category="frontend", level=4),
    Skill.objects.create(name="JavaScript", category="frontend", level=3),
    Skill.objects.create(name="PostgreSQL", category="database", level=3),
]

# 技術の作成
technologies = [
    Technology.objects.create(name="Python"),
    Technology.objects.create(name="Django"),
    Technology.objects.create(name="Bootstrap"),
    Technology.objects.create(name="PostgreSQL"),
]

# プロジェクトの作成
project = Project.objects.create(
    title="ポートフォリオサイト",
    description="Djangoを使用したポートフォリオサイトの開発",
    start_date="2024-01-01",
    is_ongoing=True,
    github_url="https://github.com/example/portfolio"
)
project.technologies.add(*technologies)

# 学歴の作成
Education.objects.create(
    school_name="〇〇大学",
    degree="情報工学部 情報工学科",
    field_of_study="コンピュータサイエンス",
    start_date="2020-04-01",
    end_date="2024-03-31",
    is_current=False,
    description="Webアプリケーション開発の研究に従事"
)

# 職務経歴の作成
experience = Experience.objects.create(
    company_name="株式会社〇〇",
    position="Python開発者",
    start_date="2024-04-01",
    is_current=True,
    description="Djangoを使用したWebアプリケーションの開発"
)
experience.technologies.add(*technologies)

print("サンプルデータの追加が完了しました。") 