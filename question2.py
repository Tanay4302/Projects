import os
import django

# Set DJANGO_SETTINGS_MODULE to point to the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()

# imports and code go below
from django.contrib.auth.models import User
import threading

# code for testing signals and threads

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Simulate user creation
user = User.objects.create(username="threadtest")
print(f"Main thread: {threading.current_thread().name}")
