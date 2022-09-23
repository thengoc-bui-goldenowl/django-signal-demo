from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=50)
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return "{} - {}".format(self.model, self.name)

    def save(self, *args, **kwargs):
        self.year = '2019'
        print(self.id)
        super(Car, self).save(*args, **kwargs)
        print(self.id)


@receiver(pre_save, sender=Car)
def before_save(sender, instance, **kwargs):
    print(f"Before Saving: {instance.id}")
    if hasattr(instance, 'year'):
        print('Year: ', instance.year)


@receiver(post_save, sender=Car)
def after_save(sender, instance, **kwargs):
    print(f"After Saving: {instance.id}")


def my_callback(sender, **kwargs):
    print("This is a signal function using Connecting receiver functions")


pre_save.connect(my_callback, sender=Car)
