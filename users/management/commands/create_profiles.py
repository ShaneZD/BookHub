from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile

class Command(BaseCommand):
    help = 'Create profiles for users who don’t have one'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created profiles for all users.'))
