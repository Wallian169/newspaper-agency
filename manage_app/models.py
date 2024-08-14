from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"


class Topic(models.Model):
    name = models.CharField(
        max_length=255
    )


class Newspaper(models.Model):
    title = models.CharField(
        max_length=150
    )
    content = models.TextField()
    published_date = models.DateField()
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="publishers"
    )
    topics = models.ManyToManyField(Topic, related_name="topics")
