import sys
import os
import django

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.local")
django.setup()

User = get_user_model()

#  Update the users in this list.
#  Each tuple represents the username, password, and email of a user.
users = [
    ('user1', 'todo', 'user_1@example.com'),
    ('user2', 'todo', 'user_2@example.com'),
]

for username, password, email in users:
    try:
        print('Creating user')
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        assert authenticate(username=username, password=password)
        print('User {0} successfully created.')
    except:
        print('There was a problem creating the user: {0}.  Error: {1}.')
