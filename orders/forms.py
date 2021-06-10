from django import forms
from orders.widgets import BootstrapDateTimePickerInput


class PeriodForm(forms.Form):
    start_period = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )
    end_period = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput(),
    )


