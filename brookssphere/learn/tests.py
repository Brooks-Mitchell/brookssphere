"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from urllib import response
import django
from django.test import TestCase
from django.contrib.auth.models import User

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
        
        self.client.login(username='testuser', password='testpass9!')
        response = self.client.post('/learn/', {'email': 'Changed@email.com' })
        self.assertEqual(response.status_code, 200)