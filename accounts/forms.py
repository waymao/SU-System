from django import forms
# from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(label="旧密码", widget=forms.PasswordInput())
    new_password = forms.CharField(label="新密码", widget=forms.PasswordInput())
    repeated_new_password = forms.CharField(label="重复新密码", widget=forms.PasswordInput())


class UserInfoChangeForm(forms.Form):
    last_name = forms.CharField(label="姓")
    first_name = forms.CharField(label="名")

    gender = forms.ChoiceField(label="性别",
                               choices=(
                                   ("M", "男"),
                                   ("F", "女"),
                                   ("O", "其他"),
                               ))
