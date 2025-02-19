from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
import json

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_custom_fields(sender, instance, created, **kwargs):
    if created:
        instance.comments = json.dumps({})
        instance.favorites = json.dumps([])
        instance.save()