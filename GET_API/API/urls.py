from django.urls import path
from .views import API_get_data

urlpatterns = [
    path('get_data/',API_get_data,name='get_data')
]
