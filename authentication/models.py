from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goals = models.JSONField(default=list)
    # resources = models.ManyToManyField(
    #     Article,
    #     related_name='student_resources',
    #     blank=True)

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
    @receiver(post_save, sender=User)
    def create_student_profile(sender, instance, created, **kwargs):
        if created:
            StudentProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.studentprofile.save()
