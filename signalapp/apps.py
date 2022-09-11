from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save
# from signalapp.models import Car


class SignalappConfig(AppConfig):
    name = 'signalapp'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
