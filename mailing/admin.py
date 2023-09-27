from django.contrib import admin

from mailing.models import Client, Message, EmailLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body')


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('message', 'status', 'last_attempt_time')




