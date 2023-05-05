"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from urllib import response
import django
from django.test import TestCase
from django.contrib.auth.models import User

import sys
sys.path.append('.')
from app.forms import UserForm
from django.http import HttpRequest


# TODO: Configure your database in settings.py and sync before running tests.

class LearnTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(LearnTest, cls).setUpClass()
        django.setup()


     #test profile change
    def test_profile_update(self):
        user = User.objects.create_user(username='testuser', email='user@example.com', password='testpass9!')
        
        userform = UserForm(instance=user, data={'email': 'Changed@email.com'})

        if userform.is_valid():
            user = UserForm.save()
            self.assertEquals(User.objects.get(username='testuser').email, "Changed@email.com")
        else:
            print("go to sleep")