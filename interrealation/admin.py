from django.contrib import admin
from interrealation.models import QuickRequest
# Register your models here.



@admin.register(QuickRequest)
class QuickRequestAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'name', 'my_own_price', 'no_price', 'symptoms', 'file_qr'
	]

	search_fields = ['id', 'name', 'my_own_price', 'no_price', 'symptoms', 'doc_relation' ]
	list_filter = ['name', 'my_own_price', 'no_price', 'symptoms']

