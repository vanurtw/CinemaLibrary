from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

ACTION_CREATE = 'Создал'
ACTION_UPDATE = 'Изменил'
ACTION_DELETE = 'Удалил'


class ChangeLog(models.Model):
    ACTION = [
        (ACTION_CREATE, 'Создал'),
        (ACTION_UPDATE, 'Изменил'),
        (ACTION_DELETE, 'Удалил')
    ]
    action = models.CharField(choices=ACTION, max_length=50, null=True, verbose_name='Действие')
    model = models.CharField(max_length=255, null=True, verbose_name='Имя модели')
    record_id = models.IntegerField(null=True, verbose_name='ID записи')
    data_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    data = models.JSONField(default=dict, verbose_name='Измененные данные', null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, verbose_name='Пользователь')

    class Meta:
        ordering = ['data_create']
