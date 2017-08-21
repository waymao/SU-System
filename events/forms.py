from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

class eventChangeForm(forms.Form):
    time = forms.DateTimeField(widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
