from django.contrib import admin
from models import User, UserBioDetails
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'profile_image']

@admin.register(UserBioDetails)
class UserBioDetailsAdmin(admin.ModelAdmin):
	list_display = ['id', 'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday', 'telephone_number', 'address',
	                'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases', 'surgery',
	                'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height', 'weight',
	                'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments']

