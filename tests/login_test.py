from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import User
from profiles.serializers import *
import json

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account_viewset')
        data = {'username': 'DabApps', 'password': 'pass', 'email': 'testet@test.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'DabApps')

    def test_user_login_fail(self):
        """
        checking user login on fail
        """
        url = reverse('user_login')
        data = {'username': 'DabApps', 'password': 'pass'}
        response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'error': 'The username or password was incorrect.'})

    def test_user_login_success(self):
        """
        checking user login on success
        """
        user = get_user_model().objects.create_user(username='DabApps', email='test@test.com')
        user.set_password('pass')
        user.save()
        url = reverse('user_login')
        data = {'username': 'DabApps', 'password': 'pass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
