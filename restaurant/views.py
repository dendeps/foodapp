from django.utils.timezone import datetime
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.
from customer.models import Order


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):

        # get the current date
        today = datetime.today()
        orders = Order.objects.filter(created_on__contains=today.date())

        # loop through the orders and add the price value
        total_revenue = 0
        for order in orders:
            total_revenue+=order.price

        # pass the total number of orders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='staff').exists()
