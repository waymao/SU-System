from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class eventChangeForm(forms.Form):
    time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(eventChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'eventChangeForm'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = './'

        self.helper.add_input(Submit('提交', 'Submit'))

