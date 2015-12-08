from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from interrealation.models import QuickRequest
from interrealation.serializers import *
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class QuickPostViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, id=None):
		if request.user.is_staff:
			queryset = QuickRequest.objects.all()
			serializer = QuickRequestSerializer(queryset, many=True)
			data = {
				'all_data': serializer.data,
			}
			return Response(data, status=status.HTTP_200_OK)

		if id:
			try:
				queryset = QuickRequest.objects.filter(id=id)
				serializer = QuickRequestSerializer(queryset, many=True)
				data = {
					'all_data': serializer.data,
				}
				return Response(data, status=status.HTTP_200_OK)
			except QuickRequest.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

