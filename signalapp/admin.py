from django.contrib import admin
from .models import Car
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)

# @receiver(pre_save, sender=Car)
# def before_save(sender, instance, **kwargs):
#     print(f"Before Saving: {instance.id}")
#     if hasattr(instance, 'year'):
#         print('Year: ', instance.year)


# @receiver(post_save, sender=Car)
# def after_save(sender, instance, **kwargs):
#     print(f"After Saving: {instance.id}")


# def my_callback(sender, **kwargs):
#     print("This is a signal function using Connecting receiver functions")


# pre_save.connect(my_callback, sender=Car)
