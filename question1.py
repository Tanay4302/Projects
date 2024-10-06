import os
import django

# Set DJANGO_SETTINGS_MODULE to point to the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received, starting work...")
    time.sleep(5)  # Simulating a long task
    print("Signal processing finished.")

# In some other part of the code, the signal is triggered when a User object is saved.
user = User.objects.create(username="testuser")
print("User created.")
