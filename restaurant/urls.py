from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('restaurant/dashboard', Dashboard.as_view(), name='dashboard')
]