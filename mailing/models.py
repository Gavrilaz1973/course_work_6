from django.db import models

import users
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='ФИО', **NULLABLE)
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Message(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]
    STATUS_CHOICES = [
        ('created', 'создана'),
        ('launched', 'запушена'),
        ('finished', 'завершена'),
    ]

    theme = models.CharField(max_length=150, **NULLABLE, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')
    client = models.ManyToManyField(Client, verbose_name='Получатели')
    time = models.TimeField(verbose_name='Время рассылки', **NULLABLE)
    period = models.CharField(max_length=100, choices=PERIOD_CHOICES, default=PERIOD_CHOICES[0],
                              verbose_name='Периодичность')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0], verbose_name='Статус')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class EmailLog(models.Model):
    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failure', 'Не успешно'),
    ]
    last_attempt_time = models.DateTimeField(
        auto_now=True,
        verbose_name='время последней попытки')
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name='статус')
    server_response = models.TextField(
        **NULLABLE,
        verbose_name='ответ почтового сервера')
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name='email_log',
        verbose_name='сообщение'
    )

    def __str__(self):
        return self.status, self.last_attempt_time

    class Meta:
        verbose_name = 'Логи рассылка'
        verbose_name_plural = 'Логи рассылки'


