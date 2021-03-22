from django.contrib import admin
from .models import *
from django import forms
import hashlib
import random


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data.get('title')
        hash = hashlib.sha256(str(data).encode()).hexdigest()
        self.cleaned_data['linkkey'] = hash + '@' + str(random.randrange(1000, 9999))
        return self.cleaned_data


class CustomBlog(admin.ModelAdmin):
    form = BlogForm

    list_display = ('title', 'writer', 'datetime', 'allowed', 'type')
    search_fields = ('title', 'type')


admin.site.register(Blog, CustomBlog)
admin.site.register(Tag)
admin.site.register(Resource)
admin.site.register(BlogSeries)
