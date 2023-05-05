
import django
from django.test import TestCase
from django.urls import reverse

from django.test import Client
from django.contrib.auth.models import User
from django.http import HttpResponse


class SignupTest(TestCase):
    
    # Django requires an explicit setup() when running tests in PTVS (Python Tools for Visual Studio)
    @classmethod
    def setUpClass(cls):
        super(SignupTest, cls).setUpClass()
        user = User.objects.create_user('TestUser', 'test@testmail.com', 'TestPass')
        django.setup()

    def test_login(self):

        # log in with the user we created in the setup above
        self.client.login(username='TestUser', password='TestPass')
        response = self.client.get('/login/', follow=True)
        # set user to object retrieved from db where username = 'TestUser'
        user = User.objects.get(username='TestUser')
        self.assertEqual(response.context['user'].username, 'TestUser')

    # TODO - second test not working with user created in setUpClass     
    def test_profile_creation(self):
        user = User.objects.create_user('TestUser2', 'test@testmail.com2', 'TestPass2')
        self.assertEqual(user.profile.profile_name, 'name')