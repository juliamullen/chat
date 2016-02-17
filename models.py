from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=1000)
    image = models.ImageField()
    date = models.DateTimeField()
