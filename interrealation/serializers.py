from rest_framework import serializers
from interrealation.models import QuickRequest


class QuickRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuickRequest
		fields = ('id', 'name', 'my_own_price', 'no_price', 'symptoms', 'file_qr', 'doc_relation')
