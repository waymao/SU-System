from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class clubChangeForm(forms.Form):
    description = forms.CharField(label="", widget=CKEditorUploadingWidget())


class clubCreateForm(forms.Form):
    name = forms.CharField(label="名称")
    description = forms.CharField(label="", widget=CKEditorUploadingWidget())
