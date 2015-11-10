import re
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from profiles.models import User, UserBioDetails
from django.core import validators


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'url', 'username', 'email')


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30,
                                     validators=[
                                         validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid username.',
                                                                   'invalid'),
                                         UniqueValidator(queryset=User.objects.all(),
                                                         message='This username already exists.')]
                                     )
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
                                         validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                   'Username format is not valid.',
                                                                   'invalid')]
                                     )

    password = serializers.CharField()


class UserBioDetailsSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.HyperlinkedIdentityField('avatar')

    class Meta:
        model = UserBioDetails
        fields = (
            'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday', 'telephone_number', 'address',
            'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases', 'surgery',
            'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height', 'weight',
            'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments', 'relation_to_user_model'
        )


class UserBioDetailsSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = UserBioDetails
        fields = (
            'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday', 'telephone_number', 'address',
            'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases', 'surgery',
            'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height', 'weight',
            'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments'
        )
