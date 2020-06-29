from django.db import models
from django.contrib.auth.admin import User


class Blog(models.Model):
    CHOICES =[('Technology', 'Technology'),('Privacy', 'Privacy'),('Security', 'Security'),]
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=160,)
    image = models.ImageField()
    subtitle = models.CharField(max_length=256)
    text = models.CharField(max_length=4000)
    link = models.URLField(default='google.com')
    top3 = models.BooleanField(default=False)
    allowed = models.BooleanField(default=False)
    type = models.CharField(max_length=24,choices=CHOICES, null=True, blank=True, default=None)