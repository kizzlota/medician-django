from django.contrib.auth import get_user_model
from rest_framework import serializers
import re
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core import validators
from models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'url', 'username', 'email')



class AccountSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=30,
                                  validators=[

                                      UniqueValidator(queryset=User.objects.all(),
                                                      message='User with this Email address already exists.'),
                                      validators.EmailValidator()]
                                  )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

        # def __init__(self, *args, **kwargs):
        # super(AccountSerializer, self).__init__(*args, **kwargs)
        #     print self.fields['email'].validators


class AccountLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30,
                                     validators=[
                                         validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Username format is not valid.',
                                                                   'invalid')]
                                     )

    password = serializers.CharField()

