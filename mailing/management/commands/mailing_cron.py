from django.core.management import BaseCommand

from mailing.services import cronjob_daily, cronjob_weekly, cronjob_monthly


class Command(BaseCommand):

    def handle(self, *args, **options):
        cronjob_daily()
        cronjob_weekly()
        cronjob_monthly()
