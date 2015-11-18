from django.contrib import admin
from models import User, UserBioDetails, UserAnalyzes, UserFiles, DocCategories, DocProfile, UserAddress
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined',
	                'profile_image']
	search_fields = ['id', 'username', 'email', 'first_name']
	list_filter = ['id', 'username', 'email']


@admin.register(UserBioDetails)
class UserBioDetailsAdmin(admin.ModelAdmin):
	list_display = ['id', 'avatar', 'name', 'second_name', 'surname', 'ident_code', 'sex', 'birthday',
	                'telephone_number', 'address',
	                'invalidity', 'blood_type', 'rh_factor', 'blood_transfusion', 'diabetes', 'infections_diseases',
	                'surgery',
	                'allegric_history', 'medicinal_intolerance', 'vaccinations', 'previous_diagnosis', 'height',
	                'weight',
	                'sport_life', 'bad_habits', 'special_nutrition', 'user_additional_comments']

	search_fields = ['id', 'name', 'telephone_number', 'surname']
	list_filter = ['id', 'name']
	raw_id_fields = ('relation_to_user',)



@admin.register(UserAnalyzes)
class UserAnalyzesAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'date_of_analyzes', 'title_analyzes', 'everything_data', 'relation_to_user_files'
	]

	search_fields = ['id', 'date_of_analyzes', 'title_analyzes']
	list_filter = ['date_of_analyzes', 'title_analyzes']
	date_hierarchy = 'date_of_analyzes'


@admin.register(UserFiles)
class UserFilesAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'file', 'date_of_add', 'name_file'
	]
	search_fields = ['id', 'file', 'date_of_add', 'name_file']
	list_filter = ['file', 'date_of_add', 'name_file']
	date_hierarchy = 'date_of_add'


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


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'phone', 'address', 'city', 'street', 'country'
	]
	search_fields = ['id', 'phone', 'address', 'city']
	list_filter = ['phone', 'address', 'city']
