from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import User, UserFiles, DocCategories
from interrealation.models import QuickRequest
from profiles.serializers import *
from rest_framework.test import force_authenticate
import json
from rest_framework.test import APIRequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile, InMemoryUploadedFile
import StringIO
from PIL import Image


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


class QuickRequestTests(APITestCase):
	"""
    Testing quick ruequest functinality.
    """

	def test_create(self):
		'''
		testing creating quick request
		'''
		user = get_user_model().objects.create_user(username='DabApps', email='test@test.com')
		user.set_password('pass')
		user.is_staff = True
		user.save()
		self.client.login(username='DabApps', password='pass')
		file_element = get_temporary_image()
		url = reverse('quick_post')
		data = {'name': 'req1_kizzlota1', 'my_own_price': '0', 'symptoms': 'no symptoms', 'file_qr': file_element,
		        'user_relation': user.id}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_quick_request_with_id(self):
		'''
		testing updating quick request by posting url with id
		'''
		user = get_user_model().objects.create_user(username='DabApps', email='test@test.com')
		user.set_password('pass')
		user.is_staff = True
		user.save()
		self.client.login(username='DabApps', password='pass')
		file_element = get_temporary_image()
		quick_request = QuickRequest.objects.create(name='test_request', my_own_price='100', symptoms='test symptoms', file_qr=file_element, user_relation=user)
		quick_request.save()
		url_sub = '/api/quick_post/{0}/'.format(quick_request.id)
		file_update = get_temporary_image()
		data = {'name': 'test_request_updated', 'my_own_price': '200', 'symptoms': 'updated_symp', 'file_qr': file_update, 'user_relation': user.id}
		response = self.client.post(url_sub, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response_data = 'test_request_updated'
		self.assertEqual(response.data['name'], response_data)


