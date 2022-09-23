from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Car


@receiver(pre_save, sender=Car)
def pre_save_func(sender, **kwargs):
    print("Before Save in signals")


@receiver(post_save, sender=Car)
def pre_save_func(sender, **kwargs):
    print("After Save in signals")

def my_callback(sender, **kwargs):
    print("This is a signal function using Connecting receiver functions in ready")
pre_save.connect(my_callback, sender=Car)

from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback1(sender, **kwargs):
    print("Request finished!")


from django import dispatch

some_task_done = dispatch.Signal()

def test():
    some_task_done.send(sender="Completed", task_id="123")


@receiver(some_task_done)
def my_task_done(sender, **kwargs):
    if 'task_id' in kwargs:
        print(kwargs['task_id'])
