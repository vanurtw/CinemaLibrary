from django.db import models
from django.contrib.auth import get_user_model
from .mixins import ChangLoggableMixin

# Create your models here.

ACTION_CREATE = 'Создал'
ACTION_UPDATE = 'Изменил'
ACTION_DELETE = 'Удалил'


class ChangeLog(ChangLoggableMixin, models.Model):
    ACTION = [
        (ACTION_CREATE, 'Создал'),
        (ACTION_UPDATE, 'Изменил'),
        (ACTION_DELETE, 'Удалил')
    ]
    action = models.CharField(choices=ACTION, max_length=50, null=True, verbose_name='Действие', blank=True)
    model = models.CharField(max_length=255, null=True, verbose_name='Имя модели', blank=True)
    record_id = models.IntegerField(null=True, verbose_name='ID записи', blank=True)
    data_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания', blank=True)
    data = models.JSONField(default=dict, verbose_name='Измененные данные', null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, verbose_name='Пользователь', blank=True)

    class Meta:
        ordering = ['data_create']
        verbose_name = 'История'
        verbose_name_plural = 'История'


