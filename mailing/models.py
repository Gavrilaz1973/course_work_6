from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    # message = models.ManyToManyField(Message, verbose_name='Сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Message(models.Model):
    theme = models.CharField(max_length=150, **NULLABLE, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')
    client = models.ManyToManyField(Client, verbose_name='Получатели')


    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Settings(models.Model):
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
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    time = models.TimeField(verbose_name='Время рассылки')
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES,default=PERIOD_CHOICES[0], verbose_name='Периодичность')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0], verbose_name='Статус')


    def __str__(self):
        return f"{self.message} {self.status}"

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'




#
#
# class Logg(models.Model):
#     datetime = models.DateTimeField(verbose_name='Последняя попытка')
#     status = models.CharField(verbose_name='Статус попытки')
#     answer = models.CharField(**NULLABLE, verbose_name='Ответ сервера')
#


