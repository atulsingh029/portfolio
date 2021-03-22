from django.urls import path
from .views import blog, blogView, get



urlpatterns = [
    path('',blog),
    path('g/',blogView),
    path('get/<str:obj>', get),
]

