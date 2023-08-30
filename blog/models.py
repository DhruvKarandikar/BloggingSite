from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# type of creating backbone for the blogging site and this class creates the database columns names like Id for
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
