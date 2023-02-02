from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.user
