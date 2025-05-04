from django.core.management.base import BaseCommand
from users.models import User
from datetime import date

class Command(BaseCommand):
    help = 'Creates test users for development'

    def handle(self, *args, **options):
        test_users = [
            {
                'username': 'test_patient1',
                'first_name': 'John',
                'last_name': 'Doe',
                'date_of_birth': date(1990, 1, 1),
                'role': 'patient'
            },
            {
                'username': 'test_patient2',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'date_of_birth': date(1985, 5, 15),
                'role': 'patient'
            },
            {
                'username': 'test_patient3',
                'first_name': 'Ahmet',
                'last_name': 'Yılmaz',
                'date_of_birth': date(1975, 3, 20),
                'role': 'patient'
            }
        ]

        for user_data in test_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'User already exists: {user.username}')) 