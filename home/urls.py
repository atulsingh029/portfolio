from django.urls import path
from .views import *


urlpatterns = [
    path('contact/', contact),
    path('certifications/', certifications),
    path('project/<int:id>', view_project),
]