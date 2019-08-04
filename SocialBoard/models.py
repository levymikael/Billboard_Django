from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
        post_title = models.CharField(max_length = 120)
        post_publish_date = models.DateTimeField(auto_now_add=True)
        post_content = models.CharField(max_length = 500)
        post_author = models.CharField(max_length = 24)



