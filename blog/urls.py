from django.urls import path
from .views import blog,blogView



urlpatterns = [
    path('',blog),
    path('g/',blogView),
]

