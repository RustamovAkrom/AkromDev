from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from apps.users.models import UserAccount


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        self.create_superuser(
            User,
            "Akrom",
            "Rustamov",
            "Akromjon",
            "rustamovakromjon56@gmail.com",
            "2007",
        )

    def create_superuser(self, User, first_name, last_name, username, email, password):
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            UserAccount.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email
            )
            self.stdout.write(
                self.style.SUCCESS(f"Superuser {username} successfully created.")
            )
        else:
            self.stdout.write(self.style.ERROR(f"Superuser {username} already exists."))
