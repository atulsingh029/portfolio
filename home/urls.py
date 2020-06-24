from django.urls import path
from .views import *


urlpatterns = [
    path('p/',presence),
    path('c/',contact),
]