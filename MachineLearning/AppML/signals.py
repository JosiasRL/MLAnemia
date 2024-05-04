from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


@receiver(post_save, sender=Profile)
def add_user_to_medic_group(sender, instance, created, **kwargs):
    if created:
        try:
            medics = group = Group.objects.get(name='medico')
            
        except Group.DoesNotExist:
            medics = group = Group.objects.create(name='analista')
            medics = group = Group.objects.create(name='medico')
            
        instance.user.groups.add(medics) 
            