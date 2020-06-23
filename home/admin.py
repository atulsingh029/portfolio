from django.contrib import admin
from .models import Visitor,Contact,Carousel,ProjectCards,Tracking_Logger


# Register your models here.
class CustomVisitor(admin.ModelAdmin):
    list_display = ['name', 'email', 'subscribe']
    list_filter = ('subscribe', 'date')
    search_fields = ('name', 'email')


admin.site.register(Visitor,CustomVisitor)


class CustomContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'readstatus', 'datetime']
    search_fields = ['name','email', 'datetime']


admin.site.register(Contact,CustomContact)


class CustomCraousel(admin.ModelAdmin):
    list_display = ('name', 'allowed')
    list_filter = ('allowed',)
    search_fields = ('name',)


admin.site.register(Carousel,CustomCraousel)


class CustomProjectCard(admin.ModelAdmin):
    list_display = ('name', 'allowed')
    list_filter = ('allowed',)
    search_fields = ('name',)

admin.site.register(ProjectCards,CustomProjectCard)


class CustomTrackingLogger(admin.ModelAdmin):
    list_display = ('refer', 'ip', 'datetime')
    search_fields = ('refer',)

admin.site.register(Tracking_Logger,CustomTrackingLogger)