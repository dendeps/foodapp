import json

from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail


# Create your views here.
from .models import MenuItem, Order, Category


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class OrderView(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category:
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        dessert = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        mains = MenuItem.objects.filter(category__name__contains='Main')

        # pass into context
        context = {
            'appetizers': appetizers,
            'desserts': dessert,
            'drinks': drinks,
            'mains': mains
        }

        # render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        order_items = []

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items.append(item_data)

        price = 0
        item_ids = []

        for item in order_items:
            price += item.get('price')
            item_ids.append(item.get('id'))

        order = Order.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            state=state,
            city=city,
            zipcode=zipcode)
        order.items.add(*item_ids)
        #for item_id in item_ids:
        #    order.items.add(MenuItem.objects.get(id=item_id))

        body = "Thank you for the order! your food is on a way! \n" + f"Your total: {price}"
        # after creating the order, send an email:
        send_mail('Thank you for your order!',
                  body,
                  'food@app.com',[email], fail_silently=False
                    )

        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items.all(),
            'price': order.price,
        }
        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['isPaid']:
            order = Order.objects.get(pk=pk)
            order.ispaid = True
            order.save()
        return redirect('payment-confirmation')


class OrderPayConfirmation(View):
    def get(self, request):
        return render(request, 'customer/order_pay_confirmation.html')
