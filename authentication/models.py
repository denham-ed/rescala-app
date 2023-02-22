from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    goals = JSONField(default=list)
    resources = models.ManyToManyField(
        Article,
        related_name='student_resources',
        blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
