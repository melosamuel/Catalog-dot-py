from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse

class TestModelUsers(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='tester', 
            password='1234', 
            first_name='Tester', 
            last_name='Pygram', 
            email='tester@pygram.com', 
            is_active=True,
            is_staff=False,
            is_superuser=False,
            date_joined=timezone.now())
        
        self.client = Client()

    def test_user_can_login(self):
        form_data = {
            'username': self.user.username,
            'password': '1234'
        }

        response = self.client.post(reverse('login'), data=form_data)

        self.assertRedirects(response, reverse('messenger'))

    def test_user_cannot_login_without_username(self):
        self.user.username = ''

        form_data = {
            'username': self.user.username,
            'password': '1234'
        }

        response = self.client.post(reverse('login'), data=form_data)
        self.assertRedirects(response, '/auth/login?err=True')
        

    def test_user_cannot_login_with_wrong_password(self):
        form_data = {
            'username': self.user.username,
            'password': ''
        }
        response = self.client.post(reverse('login'), data=form_data)
        self.assertRedirects(response, '/auth/login?err=True')

    def test_user_needs_to_login_before_acessing_the_messenger_page(self):
        ...