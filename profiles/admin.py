from django.contrib import admin
from models import User, UserBioDetails, UserAnalyzes, UserFiles, UserActivity, DocCategories, DocProfile
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined',
	                'profile_image']

@admin.register(UserBioDetails)
class UserBioDetailsAdmin(admin.ModelAdmin):
	list_display = ['id', 'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday',
	                'telephone_number', 'address',
	                'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases',
	                'surgery',
	                'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height',
	                'weight',
	                'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments']


@admin.register(UserAnalyzes)
class UserAnalyzesAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'date_of_analyzes', 'title_analyzes', 'everything_data', 'relation_to_user_files'
	]


@admin.register(UserFiles)
class UserFilesAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'file', 'date_of_add', 'name_file'
	]


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'relation_to_user_bio', 'relation_to_analyzes', 'relation_to_user'
	]

@admin.register(DocCategories)
class DocCategoriesAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'name'
	]

@admin.register(DocProfile)
class DocProfileAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'name', 'second_name', 'surname', 'photo', 'place_of_work', 'description', 'education', 'status', 'cost',
		'certificates', 'experience'
	]