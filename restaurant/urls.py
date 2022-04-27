from django.urls import path
from .views import Dashboard, OrderDetails

urlpatterns = [
    path('restaurant/dashboard', Dashboard.as_view(), name='dashboard'),
    path('restaurant/orders/<int:pk>', OrderDetails.as_view(), name='order-details'),
]