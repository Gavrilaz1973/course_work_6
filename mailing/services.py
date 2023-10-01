from config import settings
from mailing.models import Message, EmailLog
from django.core.mail import send_mail


def send_email(email):

    try:
        send_mail(
            subject=email.theme,
            message=email.body,
            recipient_list=[client.email for client in email.client.all()],
            from_email=settings.EMAIL_HOST_USER
            )
    except Exception as error:
        email_log = EmailLog.objects.create(
            status='failure', server_response=error, message=email)
        email_log.save()
    else:
        email_log = EmailLog.objects.create(
            status='success', server_response='Sent successfully', message=email)
        email_log.save()


def cronjob_daily():
    emails = Message.objects.all()
    for email in emails:
        if email.status == 'finished':
            continue
        if email.period == 'daily':
            send_email(email)
            email.status = 'launched'
            email.save()


def cronjob_weekly():
    emails = Message.objects.all()
    for email in emails:
        if email.period == 'weekly':
            send_email(email)
            email.status = 'launched'
            email.save()


def cronjob_monthly():
    emails = Message.objects.all()
    for email in emails:
        if email.period == 'monthly':
            send_email(email)
            email.status = 'launched'
            email.save()



