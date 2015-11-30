from django.shortcuts import render
from models import User, UserAddress
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *
from forms import RegisterForm, RegisterFormSecond
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from profiles.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# from profiles.mailing import send_email
# Create your views here.

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = get_user_model().objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class AccountViewSet(viewsets.ViewSet):
	permission_classes = (AllowAny,)

	# authentication_classes = (JSONWebTokenAuthentication, )

	def create(self, request):

		serializer = AccountSerializer(data=request.data)
		if serializer.is_valid():

			username = serializer.data['username']
			email = serializer.data['email']
			password = serializer.data['password']

			# Creating an user entry

			user = get_user_model().objects.create_user(username=username)
			user.set_password(password)
			user.email = email
			user.save()

			user1 = authenticate(username=username, password=password)
			if user1 is not None:
				login(request, user1)

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountLogin(viewsets.ViewSet):
	permission_classes = (AllowAny,)

	# authentication_classes = (JSONWebTokenAuthentication, )

	def login(self, request):
		serializer = AccountLoginSerializer(data=request.data)
		if serializer.is_valid():
			username = serializer.data['username']
			password = serializer.data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)

				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response({'error': 'The username or password was incorrect.'},
				                status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBioViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, id=None):
		if id:
			try:
				queryset = UserBioDetails.objects.filter(id=id, relation_to_user=request.user.id)
				serializer = UserBioDetailsSerializer(queryset, many=True)
				data = {
					'all_data': serializer.data,
				}
				return Response(data, status=status.HTTP_200_OK)
			except UserBioDetails.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		else:
			queryset = UserBioDetails.objects.filter(name=request.user.id)
			serializer = UserBioDetailsSerializer(queryset, many=True)
			data = {
				'all_data': serializer.data,
			}
			return Response(data)

	def create(self, request, id=None):
		if id:
			try:
				instance = UserBioDetails.objects.get(id=id, relation_to_user=request.user.id)
			except UserBioDetails.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

			serializer = UserBioDetailsSerializer(instance=instance, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		else:
			request.data['relation_to_user'] = request.user.id
			serializer = UserBioDetailsSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()

				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAddressViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, id=None):
		if id:
			try:
				queryset = UserAddress.objects.filter(id=id)
				serializer = UserAddressSerializer(queryset, many=True)
				data = {
					'all_data': serializer.data,
				}
				return Response(data, status=status.HTTP_200_OK)
			except UserAddress.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		else:
			queryset = UserAddress.objects.filter(id=request.user.id)
			serializer = UserAddressSerializer(queryset, many=True)
			data = {
				'all_data': serializer.data,
			}
			return Response(data)

	def create(self, request, id=None):
		if id:
			try:
				instance = UserAddress.objects.get(id=id)
			except UserAddress.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

			serializer = UserAddressSerializer(instance=instance, data=request.data)
		else:
			serializer = UserAddressSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserAnalyzesViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, id=None):
		if id:
			try:
				queryset = UserAnalyzes.objects.filter(id=id)
				serializer = UserAnalyzesSerializer(queryset, many=True)
				data = {
					'all_data': serializer.data,
				}
				return Response(data, status=status.HTTP_200_OK)
			except UserAnalyzes.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		else:
			queryset = UserAnalyzes.objects.filter(id=request.user.id)
			serializer = UserAnalyzesSerializer(queryset, many=True)
			data = {
				'all_data': serializer.data,
			}
			return Response(data)

	def create(self, request, id=None):
		try:
			instance = UserAnalyzes.objects.get(id=id)
		except UserAnalyzes.DoesNotExist, e:
			return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

		serializer = UserAnalyzesSerializer(instance=instance, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFilesViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, id=None):
		if id:
			try:
				queryset = UserFiles.objects.filter(id=id)
				serializer = UserFilesSerializer(queryset, many=True)
				data = {
					'all_data': serializer.data,
				}
				return Response(data, status=status.HTTP_200_OK)
			except UserFiles.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		else:
			queryset = UserFiles.objects.filter(id=request.user.id)
			serializer = UserFilesSerializer(queryset, many=True)
			data = {
				'all_data': serializer.data,
			}
			return Response(data)

	def create(self, request, id=None):
		try:
			instance = UserFiles.objects.get(id=id)
		except UserFiles.DoesNotExist, e:
			return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

		serializer = UserFilesSerializer(instance=instance, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def tester(request):
	return render(request, 'main/test.html')


def tester2(request):
	return render(request, 'main/tester2.html')


def tester3(request):
	return render(request, 'main/user_login.html')
