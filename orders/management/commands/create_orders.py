from random import randint
from decimal import Decimal
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from orders.models import (
    Order,
    OrderItem,
)


class Command(BaseCommand):
    help = 'Генерации заказов'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых заказов')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        start_created_date = datetime.strptime('01.01.2018 09:00', '%d.%m.%Y %H:%M')
        for i in range(total):
            order = Order.objects.create(
                number=i,
                created_date=start_created_date + timedelta(hours=i)
            )

            order_items = []
            for j in range(randint(1, 5)):
                order_items.append(
                    OrderItem(
                        order=order,
                        product_name=f'Товар-{randint(1, 100)}',
                        product_price=Decimal(randint(100, 9999)),
                        amount=randint(1, 100)
                    )
                )
            OrderItem.objects.bulk_create(order_items)
