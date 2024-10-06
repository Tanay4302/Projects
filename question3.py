import os
import django

# Set DJANGO_SETTINGS_MODULE to point to the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    if instance.username == "rollbackuser":
        raise Exception("Rolling back transaction.")

# Simulate a transaction block
try:
    with transaction.atomic():
        user = User.objects.create(username="rollbackuser")
        print("User created inside transaction.")
except Exception as e:
    print(f"Transaction rolled back: {e}")

# Checking if the user exists
user_exists = User.objects.filter(username="rollbackuser").exists()
print(f"User exists in the database? {user_exists}")
