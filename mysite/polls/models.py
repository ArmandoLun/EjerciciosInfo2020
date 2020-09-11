from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/', default='SOME STRING')

    def __str__(self):
        return f"{self.title} by {self.author}"
