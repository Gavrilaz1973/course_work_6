from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='ФИО', **NULLABLE)
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

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

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


