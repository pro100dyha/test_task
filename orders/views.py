from django.db.models import Sum, F
from django.views.generic import FormView
from orders.forms import PeriodForm
from orders.models import OrderItem, Order
from django.urls import reverse_lazy


class FirstPageView(FormView):
    template_name = 'orders/first.html'
    success_url = reverse_lazy('first_page')
    form_class = PeriodForm

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        context = self.get_context_data(form=form)
        dates = form.cleaned_data
        context['orders'] = Order.objects.prefetch_related('items').annotate(
            all_sum=Sum(F('items__product_price')*F('items__amount'))
        ).filter(created_date__gte=dates['start_period'], created_date__lte=dates['end_period'])
        return self.render_to_response(context)


class SecondPageView(FormView):
    template_name = 'orders/second.html'
    success_url = reverse_lazy('second_page')
    form_class = PeriodForm

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        context = self.get_context_data(form=form)
        dates = form.cleaned_data
        context['order_items'] = OrderItem.objects.select_related('order').filter(
            order__created_date__gte=dates['start_period'],
            order__created_date__lte=dates['end_period']
        ).order_by('-amount')[:20]
        return self.render_to_response(context)
