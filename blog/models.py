from django.db import models
from django.contrib.auth.admin import User


class Blog(models.Model):
    CHOICES =[('Technology', 'Technology'),('Privacy', 'Privacy'),('Security', 'Security'),]
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=160,)
    image = models.ImageField()
    subtitle = models.CharField(max_length=256)
    text = models.TextField(max_length=8000)
    linkkey = models.CharField(unique=True,max_length=255)
    top3 = models.BooleanField(default=False)
    allowed = models.BooleanField(default=False)
    type = models.CharField(max_length=24,choices=CHOICES, null=True, blank=True, default=None)

