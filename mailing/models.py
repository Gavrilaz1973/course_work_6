from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    email = models.EmailField(verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')


# class Settings(models.Model):
#     time = models.TimeField(verbose_name='Время рассылки')
#     period = models.CharField(verbose_name='Периодичность')
#     status = models.CharField(verbose_name='Статус')
#
#
# class Message(models.Model):
#     theme = models.CharField(max_length=150, **NULLABLE, verbose_name='Тема')
#     body = models.TextField(verbose_name='Сообщение')
#
#
# class Logg(models.Model):
#     datetime = models.DateTimeField(verbose_name='Последняя попытка')
#     status = models.CharField(verbose_name='Статус попытки')
#     answer = models.CharField(**NULLABLE, verbose_name='Ответ сервера')
#


