from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

    # Update the profile data with the updated user data

