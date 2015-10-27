from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
import os
from django.conf import settings
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        user = self.model(username=username, email=self.normalize_email(email),
                          last_login=now, date_joined=now, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username=username, email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAddress(models.Model):
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    street = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True,
                                help_text=_(
                                    'Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'))
    email = models.EmailField(max_length=255, unique=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_staff = models.BooleanField(default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(default=False,
                                    help_text=_(
                                        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # Additions fields
    social_img_url = models.CharField(max_length=120, blank=True, null=True)
    profile_image = models.ImageField(upload_to="uploads", blank=False, null=False,
                                      default="/static/img/users/defaultuserimage.png")

    user_bio = models.TextField(max_length=1200, blank=True)

    user_details = models.ForeignKey(UserAddress, default=1)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    # def email_user(self, subject, message, from_email=None):
    #    send_mail(subject, message, from_email, [self.email])
    def __unicode__(self):
        return self.username


class RegistrationCode(models.Model):
    code = models.CharField(max_length=255)
    username = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('user_image', filename)


class UserBioDetails(models.Model):
    avatar = models.ImageField(blank=True, null=True, upload_to=get_file_path,
                               default="/static/img/defaultuserimage.jpeg")
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ident_code = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    invalidity = models.CharField(max_length=200, blank=True, null=True)
    blood_type = models.IntegerField(blank=True, null=True)
    rh_factor = models.BooleanField()
    blood_transfusion = models.BooleanField()
    diabetes = models.BooleanField()
    infections_diseases = models.TextField(max_length=500, blank=True, null=True)
    surgery = models.TextField(max_length=500, blank=True, null=True)
    allegric_history = models.TextField(max_length=500, blank=True, null=True)
    medicinal_intolerance = models.TextField(max_length=500, blank=True, null=True)
    vaccinations = models.TextField(max_length=200, blank=True, null=True)
    previous_diagnosis = models.TextField(max_length=200, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.ImageField(blank=True, null=True)
    sport_life = models.TextField(max_length=200, blank=True, null=True)
    bad_habits = models.TextField(max_length=200, blank=True, null=True)
    special_nutrition = models.TextField(max_length=200, blank=True, null=True)
    user_additional_comments = models.TextField(max_length=500, blank=True, null=True)
    relation_to_user = models.ForeignKey(settings.AUTH_USER_MODEL)
