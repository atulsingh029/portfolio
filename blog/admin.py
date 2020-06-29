from django.contrib import admin
from .models import Blog

# Register your models here.
class CustomBlog(admin.ModelAdmin):
    list_display = ('title', 'writer', 'datetime' , 'top3', 'allowed','type')
    search_fields = ('title','type')


admin.site.register(Blog,CustomBlog)