from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import User
from profiles.serializers import *
from rest_framework.test import force_authenticate
import json
from rest_framework.test import APIRequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile, InMemoryUploadedFile
import StringIO
from PIL import Image


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
        user_bio = UserBioDetails.objects.create(address='Ternopil', name='user1', relation_to_user=user)
        user_bio.save()
        url1 = '/api/account/user_details/{0}/'.format(user_bio.id)
        data = {'name': 'DabApps', 'telephone_number': '123', 'address': 'Kyiv', 'relation_to_user': user.id}
        self.client.login(username='DabApps', password='pass')
        response = self.client.post(url1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = 'Kyiv'
        self.assertEqual(response.data['address'], response_data)

    def test_user_adress(self):
        user = get_user_model().objects.create_user(username='DabApps', email='test@test.com')
        user.set_password('pass')
        user.save()
        user_bio = UserAddress.objects.create(address='Ternopil', phone='1234123')
        url1 = '/api/account/user_address/{0}/'.format(user_bio.id)
        self.client.login(username='DabApps', password='pass')
        user_address = UserAddress.objects.create(phone='123', city='ternopil')
        user_address.save()
        data = {'phone': '12345', 'city': 'Ternopil'}
        response = self.client.post(url1, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = '12345'
        self.assertEqual(response.data['phone'], response_data)



def get_temporary_image():
    io = StringIO.StringIO()
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(io, format='JPEG')
    image_file = InMemoryUploadedFile(io, None, 'foo.jpg', 'jpeg', io.len, None)
    image_file.seek(0)
    return image_file

def get_temporary_text_file():
    io = StringIO.StringIO()
    io.write('foo')
    text_file = InMemoryUploadedFile(io, None, 'foo.txt', 'text', io.len, None)
    text_file.seek(0)
    return text_file


class FileUploadTests(APITestCase):

    def test_if_form_submits(self):
        user = get_user_model().objects.create_user(username='DabApps', email='test@test.com')
        user.set_password('pass')
        user.save()
        self.client.login(username='DabApps', password='pass')
        file = get_temporary_image()
        url = '/api/account/user_details/'
        response = self.client.post(url, {'file': file, 'name_file':'some_file'})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    # def test_if_form_fails_on_text_file(self):
    #     file = get_temporary_text_file()
    #     response = self.client.post(reverse('user_files'), {'image': file})
    #     self.assertEqual(200, response.status_code)
    #     error_message = 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.'
    #     self.assertFormError(response, 'form', 'image', error_message)
