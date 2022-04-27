from django.urls import path
from .views import Index, About, OrderView, OrderConfirmation, OrderPayConfirmation, Menu, MenuSearch

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about', About.as_view(), name='about'),
    path('order', OrderView.as_view(), name='order'),
    path('menu', Menu.as_view(), name='menu'),
    path('menu/search', MenuSearch.as_view(), name='menu-search'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation'),
    path('payment-confirmation', OrderPayConfirmation.as_view(), name='payment-confirmation'),
]