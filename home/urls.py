from django.urls import path
from .views import *


urlpatterns = [
    path('p/', presence),
    path('contact/', contact),
    path('collab/', collab),
    path('certifications/', certifications),
    path('projects/',projects),
    path('collab/fill/<str:id>', collab_form)
]