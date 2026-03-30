from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    npm = models.CharField(max_length=30)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)

    def __str__(self):
        return self.name


class SiteAppearance(models.Model):
    site_title = models.CharField(max_length=100, default='Website Kelompok')
    primary_color = models.CharField(max_length=20, default='#2563eb')
    background_color = models.CharField(max_length=20, default='#f8fafc')
    font_family = models.CharField(max_length=100, default='Inter')

    def __str__(self):
        return "Site Appearance"