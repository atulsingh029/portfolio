from django.db import models
from  django.db.models import Q, QuerySet
from django.contrib.auth.admin import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)

    def __str__(self):
        return self.name


class Blog(models.Model):
    CHOICES =[('Technology', 'Technology'), ('Privacy', 'Privacy'), ('Security', 'Security'),
              ('Programming', 'Programming'), ('how to', 'how to'), ]
    HTML = [('allow', 'allow'), ]
    serial_number = models.IntegerField(blank=True, null=True, default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=160,)
    image = models.ImageField(upload_to='blog/primary_image')
    subtitle = models.CharField(max_length=256)
    text = models.TextField(max_length=8000)
    linkkey = models.CharField(max_length=512, blank=True)
    allowed = models.BooleanField(default=False)
    type = models.CharField(max_length=24, choices=CHOICES, null=True, blank=True, default=None)
    allow_html = models.CharField(max_length=20, choices=HTML, null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True)
    visit_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @staticmethod
    def get_latest_blog():
        return Blog.objects.filter(allowed=True).order_by('datetime').reverse()[0]


    @staticmethod
    def get_top_blogs():
        objects = Blog.objects.filter(allowed=True).order_by('visit_count').exclude(linkkey=Blog.get_latest_blog().linkkey)
        if len(objects) <= 5:
            return objects.reverse()
        return objects.reverse()[:5]

    @staticmethod
    def get_latest_blogs(n):
        top = Blog.get_top_blogs()
        fnl_objs = []
        objects = Blog.objects.filter(allowed=True).order_by('datetime').reverse().exclude(linkkey=Blog.get_latest_blog().linkkey)
        for i in objects:
            if i in top:
                pass
            else:
                fnl_objs.append(i)
        if len(fnl_objs) <= 5:
            return fnl_objs
        return fnl_objs[:n]


class Resource(models.Model):
    CHOICES = [('image', 'image'), ('gif', 'gif'), ('js', 'js'), ('pdf', 'pdf'), ('docs', 'docs'), ('url', 'url'),
            ('other', 'other')]
    title = models.CharField(max_length=255)
    blog_resource = models.ForeignKey(Blog, on_delete=models.CASCADE)
    type = models.CharField(max_length=24, choices=CHOICES)
    file = models.FileField(upload_to='blog/resource', null=True, blank=True)
    url = models.URLField(null=True, blank=True)


class BlogSeries(models.Model):
    name = models.CharField(max_length=512)
    blogs = models.ManyToManyField(Blog)

    def __str__(self):
        return self.name

    def get_top_blog_series(self, n):
        pass

    def get_latest_series(self, n):
        pass