# Create your models here.
# try:
#     from django.contrib.auth import get_user_model
#     User = get_user_model()
# except ImportError:
#     from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()