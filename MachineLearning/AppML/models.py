from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name='Usuario')
    #image = models.ImageField(max_length=150, null=True, blank=True, upload_to="users/", verbose_name='Imagen_Perfil')
    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Apellido')
    email = models.CharField(max_length=150, null=True, blank=True, verbose_name='Correo')
    
    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        ordering=['-id']
        
    def __str__(self):
        return  self.user.username

def create_uset_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_uset_profile, sender=User)
post_save.connect(save_user_profile, sender=User)