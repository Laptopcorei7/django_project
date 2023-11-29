from django.contrib.auth.management.commands import createsuperuser
from django.core.management.base import CommandError


class Command(createsuperuser.Command):
    help = 'Creates a superuser if a superuser with the same username does not exist.'

    def handle(self, *args, **options):
        username = options.get('username')
        try:
            self.UserModel._default_manager.db_manager(
                'default').get(username=username, is_superuser=True)
        except self.UserModel.DoesNotExist:
            super().handle(*args, **options)
        else:
            raise CommandError(
                'Superuser with username "%s" already exists.' % username)
