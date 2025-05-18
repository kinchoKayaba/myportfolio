from django.db import models
from django.utils import timezone

class Profile(models.Model):
    """プロフィール情報を管理するモデル"""
    name = models.CharField('名前', max_length=100)
    title = models.CharField('職種/希望職種', max_length=200)
    bio = models.TextField('自己紹介')
    email = models.EmailField('メールアドレス')
    github_url = models.URLField('GitHub URL', blank=True)
    linkedin_url = models.URLField('LinkedIn URL', blank=True)
    twitter_url = models.URLField('Twitter URL', blank=True)
    profile_image = models.ImageField('プロフィール画像', upload_to='profile_images/', blank=True)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'プロフィール'
        verbose_name_plural = 'プロフィール'

    def __str__(self):
        return self.name

class Skill(models.Model):
    """スキル情報を管理するモデル"""
    CATEGORY_CHOICES = [
        ('frontend', 'フロントエンド'),
        ('backend', 'バックエンド'),
        ('database', 'データベース'),
        ('devops', 'DevOps'),
        ('other', 'その他'),
    ]

    name = models.CharField('スキル名', max_length=100)
    level = models.IntegerField('レベル', choices=[(i, i) for i in range(1, 6)])
    category = models.CharField('カテゴリー', max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField('作成日時', default=timezone.now)

    class Meta:
        verbose_name = 'スキル'
        verbose_name_plural = 'スキル'

    def __str__(self):
        return f"{self.name} (レベル{self.level})"

class Project(models.Model):
    """プロジェクト情報を管理するモデル"""
    title = models.CharField('プロジェクト名', max_length=200)
    description = models.TextField('説明')
    technologies = models.ManyToManyField(Skill, verbose_name='使用技術')
    github_url = models.URLField('GitHub URL', blank=True)
    demo_url = models.URLField('デモURL', blank=True)
    image = models.ImageField('プロジェクト画像', upload_to='project_images/', blank=True)
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日', null=True, blank=True)
    is_ongoing = models.BooleanField('進行中', default=False)
    created_at = models.DateTimeField('作成日時', default=timezone.now)

    class Meta:
        verbose_name = 'プロジェクト'
        verbose_name_plural = 'プロジェクト'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Education(models.Model):
    """学歴情報を管理するモデル"""
    school_name = models.CharField('学校名', max_length=200)
    degree = models.CharField('学位', max_length=200)
    field_of_study = models.CharField('専攻', max_length=200)
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日', null=True, blank=True)
    is_current = models.BooleanField('在学中', default=False)
    description = models.TextField('説明', blank=True)
    created_at = models.DateTimeField('作成日時', default=timezone.now)

    class Meta:
        verbose_name = '学歴'
        verbose_name_plural = '学歴'
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.school_name} - {self.degree}"

class Experience(models.Model):
    """職務経歴を管理するモデル"""
    company_name = models.CharField('会社名', max_length=200)
    position = models.CharField('役職', max_length=200)
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日', null=True, blank=True)
    is_current = models.BooleanField('在職中', default=False)
    description = models.TextField('説明')
    technologies = models.ManyToManyField(Skill, verbose_name='使用技術')
    created_at = models.DateTimeField('作成日時', default=timezone.now)

    class Meta:
        verbose_name = '職務経歴'
        verbose_name_plural = '職務経歴'
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.company_name} - {self.position}"

class Contact(models.Model):
    """お問い合わせ情報を管理するモデル"""
    name = models.CharField('お名前', max_length=100)
    email = models.EmailField('メールアドレス')
    subject = models.CharField('件名', max_length=200)
    message = models.TextField('メッセージ')
    created_at = models.DateTimeField('送信日時', default=timezone.now)
    is_read = models.BooleanField('既読', default=False)

    class Meta:
        verbose_name = 'お問い合わせ'
        verbose_name_plural = 'お問い合わせ'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
