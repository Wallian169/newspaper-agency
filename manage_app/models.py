from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Redactor(AbstractUser):
    years_of_experience = models.PositiveSmallIntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def get_absolute_url(self):
        return reverse("manage_app:redactor-detail", kwargs={"pk": self.pk})


class Topic(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.title
