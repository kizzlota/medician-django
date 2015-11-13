from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import User
from profiles.serializers import *
from rest_framework.test import force_authenticate
import json
from rest_framework.test import APIRequestFactory


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

    def test_user_detail(self):
        """
        testing saving user details by url
        """
        user = get_user_model().objects.create_user(username='DabApps', email='test@test.com')
        user.set_password('pass')
        user.save()
        url = reverse('user_details')
        user_bio = UserBioDetails.objects.create(address='Ternopil', name='user1', relation_to_user=user)
        user_bio.save()
        url1 = '/api/account/add/user_details/{0}/'.format(user_bio.id)
        data = {'name': 'DabApps', 'telephone_number': '123', 'address': 'Kyiv', 'relation_to_user' : user.id}
        self.client.login(username='DabApps', password='pass')
        response = self.client.post(url1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = {'previous_diagnosis': None, 'surname': None, 'weight': None, 'sex': None,
                         'allegric_history': None, 'surgery': None, 'sport_life': None, 'special_nutrition': None,
                         'user_additional_comments': None, 'blood_type': None, 'relation_to_user': 1,
                         'invalidity': None, 'bad_habits': None, 'birthday': '2015-11-13', 'vaccinations': None,
                         'address': u'Kyiv', 'height': None, 'diabetes': None, 'infections_diseases': None,
                         'name': u'DabApps', 'medicinal_intolerance': None, 'ident_code': None,
                         'blood_transfusion': None, 'telephone_number': u'123',
                         'avatar': '/static/img/defaultuserimage.jpeg', 'rh_factor': None, 'second_name': None}

        self.assertEqual(response.data, response_data)

