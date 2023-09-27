from django.core.management import BaseCommand

from mailing.services import cronjob


class Command(BaseCommand):

    def handle(self, *args, **options):
        cronjob()