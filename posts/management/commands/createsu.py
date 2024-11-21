from pathlib import Path
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
import os 

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

load_dotenv(BASE_DIR/ '.env')

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='SUPERUSER_USERNAME').exists():
            User.objects.create_superuser(
                username = os.getenv('SUPERUSER_USERNAME'),
                email = os.getenv('SUPERUSER_EMAIL'),
                password = os.getenv('SUPERUSER_PASSWORD')
            )
        print('Superuser has been created.')