from django.db.models.signals import post_save
from django.dispatch import receiver
from .mixins import ChangLoggableMixin
from .models import ChangeLog




def my_signal_test(sender,instance, created,  **kwargs):
    if isinstance(sender, ChangLoggableMixin):
        if created:
            pass
        else:
            ChangeLog.add()

