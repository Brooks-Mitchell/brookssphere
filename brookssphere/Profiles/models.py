from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=80, default="name") 
    operations_performed = models.IntegerField(default = 0)
    date_of_birth = models.DateTimeField(auto_now_add=True, blank=True)

# creates a profile linked to a User when a user account is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

 # saves the profile when calling User save method
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except:
        print("Superuser has no profile")