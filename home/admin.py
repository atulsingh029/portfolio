from django.contrib import admin
from .models import *


class CustomVisitor(admin.ModelAdmin):
    list_display = ['name', 'email', 'subscribe']
    list_filter = ('subscribe', 'date')
    search_fields = ('name', 'email')


class CustomContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'readstatus', 'datetime']
    search_fields = ['name','email', 'datetime']


admin.site.register(Contact,CustomContact)


class CustomCertification(admin.ModelAdmin):
    list_display = ['name', 'c_link', 'issue_date', 'expiry_date', 'issuedby', 'allowed']
    search_fields = ['name',]


admin.site.register(Certification,CustomCertification)


class CustomProject(admin.ModelAdmin):
    list_display = ('name', 'allowed')
    list_filter = ('allowed',)
    search_fields = ('name',)


admin.site.register(Project,CustomProject)


class CustomTrackingLogger(admin.ModelAdmin):
    list_display = ('refer', 'ip', 'datetime')
    search_fields = ('refer',)


admin.site.register(Logger, CustomTrackingLogger)


class CustomProfile(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


admin.site.register(Profile, CustomProfile)


admin.site.register(ContactIcon)


admin.site.register(Badge)

admin.site.register(Experience)

admin.site.register(TechStack)