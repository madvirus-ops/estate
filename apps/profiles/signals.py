import logging
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)
User = get_user_model()

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s Profile create")