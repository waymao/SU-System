from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class eventChangeForm(forms.Form):
    time = forms.DateTimeField(label="时间", widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
    type = forms.CharField(label="类型")
    description = forms.CharField(label="", widget=CKEditorUploadingWidget())


class eventCreateForm(forms.Form):
    name = forms.CharField(label="名称")
    time = forms.DateTimeField(label="时间", widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
    type = forms.CharField(label="类型")
    description = forms.CharField(label="", widget=CKEditorUploadingWidget())

