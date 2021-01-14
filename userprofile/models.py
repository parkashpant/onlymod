from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    Domain_Choices = [
        ('HEALTHCARE', 'Healthcare'),
        ('TECHNOLOGY', 'Technology'),
        ('FINANCE', 'Finance'),
        ('LEGAL', 'Legal'),
        ('EDUCATION', 'Education'),
        ('AGRICULTURE', 'Agriculture')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    year_of_exp = models.IntegerField()
    work_domain = models.CharField(max_length=20, choices=Domain_Choices)
    linkedin_url = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

