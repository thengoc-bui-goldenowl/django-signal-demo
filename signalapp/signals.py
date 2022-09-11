from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Car


@receiver(pre_save, sender=Car)
def pre_save_func(sender, **kwargs):
    print("Before Save")


@receiver(post_save, sender=Car)
def pre_save_func(sender, **kwargs):
    print("After Save")

def my_callback(sender, **kwargs):
    print("This is a signal function using Connecting receiver functions in ready")
pre_save.connect(my_callback, sender=Car)

