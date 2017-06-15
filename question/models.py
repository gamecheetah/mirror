from django.db import models
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    yes_answers=0
    no_answers=0

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
