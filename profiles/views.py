from django.shortcuts import render
from models import User, UserAddress
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import User
from forms import RegisterForm, RegisterFormSecond
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from profiles.serializers import *
from rest_framework.response import Response
from rest_framework import status

# from profiles.mailing import send_email
# Create your views here.

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
			email = serializer.data['email']
			password = serializer.data['password']

			# Creating an user entry

			user = get_user_model().objects.create_user(email=email)
			user.set_password(password)
			user.email = None
			user.save()

			return Response(user, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def tester(request):
	return render(request, 'main/test.html')

