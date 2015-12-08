import re
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from profiles.models import User, UserBioDetails, UserAddress, UserAnalyzes, UserFiles
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

#
# class UserBioDetailsSerializer(serializers.HyperlinkedModelSerializer):
#     avatar = serializers.HyperlinkedIdentityField('avatar')
#
#     class Meta:
#         model = UserBioDetails
#         fields = (
#             'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday', 'telephone_number', 'address',
#             'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases', 'surgery',
#             'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height', 'weight',
#             'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments', 'relation_to_user'
#         )


class UserBioDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBioDetails
        fields = (
            'id', 'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday', 'telephone_number', 'address',
            'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases', 'surgery',
            'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height', 'weight',
            'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments', 'relation_to_user'
        )


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('id', 'phone', 'address', 'city', 'street', 'country')


class UserFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFiles
        fields = ('id', 'file', 'date_of_add', 'name_file')


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class UserAnalyzesSerializer(serializers.ModelSerializer):
    #relation_to_user_files = UserFilesSerializer(many=True,)
    everything_data = JSONSerializerField()

    def create(self, validated_data):
        return UserAnalyzes.objects.create(**validated_data)

    class Meta:
        model = UserAnalyzes
        fields = ('id', 'date_of_analyzes', 'title_analyzes', 'everything_data', 'relation_to_user_files')

