from django.db.models.signals import post_save
from django.dispatch import receiver
from .mixins import ChangLoggableMixin
from .models import ChangeLog, ACTION_CREATE, ACTION_DELETE, ACTION_UPDATE
from .middlewary import LoggedInUser


def my_signal_test(sender, instance, created, **kwargs):
    if isinstance(instance, ChangLoggableMixin):
        logged_in = LoggedInUser()
        if created:
            action = ACTION_CREATE
            user = logged_in.user
            data = {}
            ChangeLog.add(instance, user, action, data)
        else:
            data = instance.change_data()
            if data:
                action = ACTION_UPDATE
                user = logged_in.current_user
                ChangeLog.add(instance, user, action, data)
