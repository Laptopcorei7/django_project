# yourapp/management/commands/collectstatic_on_deploy.py
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Collect static files during deployment'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Collecting static files...'))
        call_command('collectstatic', interactive=False)
        self.stdout.write(self.style.SUCCESS(
            'Static files collected successfully'))
