from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    GENDER_CHOICES=(
        ("m","male"),
        ("f","female"),
        ("u","undefined")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='u'
    )

# Create your models here.
