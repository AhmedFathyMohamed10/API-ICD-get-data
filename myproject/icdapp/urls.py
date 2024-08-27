from django.urls import path
from .views import get_diseases, retain_fields

urlpatterns = [
    path('get-diseases/', get_diseases, name='get_diseases'),
    path('get/', retain_fields,)
]