
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_creative == True:
            # AdminProfile.objects.create(user=instance)
            CreativeAccount.objects.create(account=instance)
            print('Profile created successfully')

        elif instance.is_user == True:
            UserAccount.objects.create(account=instance)


@receiver(post_save, sender=Account)
def update_profile(sender, instance, created, **kwargs):

    try:
        if instance.is_creative == True:
            # AdminProfile.objects.create(user=instance)
            CreativeAccount.objects.create(account=instance)
            print('Profile created successfully')

        elif instance.is_user == True:
            UserAccount.objects.create(account=instance)

    except:
        instance.useraccount = None
