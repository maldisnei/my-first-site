from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    auth = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    testo = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
