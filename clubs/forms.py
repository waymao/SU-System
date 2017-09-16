from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
import tinymce.models as tinymce_models


class clubChangeForm(forms.Form):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage


class clubCreateForm(forms.Form):
    name = forms.CharField(label="名称")
    description = forms.CharField(label="简介", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage

