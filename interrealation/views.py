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

	def status_ok(self, queryset):
		serializer = QuickRequestSerializer(queryset, many=True)
		data = {
			'all_data': serializer.data,
		}
		return Response(data, status=status.HTTP_200_OK)

	def list(self, request, id=None):
		if request.user.is_staff:
			if id:
				try:
					queryset = QuickRequest.objects.filter(id=id, user=request.user)
					return self.status_ok(queryset)

				except QuickRequest.DoesNotExist, e:
					return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
			else:
				queryset = QuickRequest.objects.all()
				return self.status_ok(queryset)
		else:
			if id:
				try:
					queryset = QuickRequest.objects.filter(id=id)
					return self.status_ok(queryset)

				except QuickRequest.DoesNotExist, e:
					return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
			else:
				queryset = QuickRequest.objects.filter(user=request.user)
				return self.status_ok(queryset)
	#
	# def list(self, request, id=None):
	# 	if request.user.is_staff:
	# 		queryset = QuickRequest.objects.all()
	# 		serializer = QuickRequestSerializer(queryset, many=True)
	# 		data = {
	# 			'all_data': serializer.data,
	# 		}
	# 		return Response(data, status=status.HTTP_200_OK)
	#
	# 	if id:
	# 		try:
	# 			queryset = QuickRequest.objects.filter(id=id)
	# 			serializer = QuickRequestSerializer(queryset, many=True)
	# 			data = {
	# 				'all_data': serializer.data,
	# 			}
	# 			return Response(data, status=status.HTTP_200_OK)
	# 		except QuickRequest.DoesNotExist, e:
	# 			return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
	#
	def create(self, request, id=None):
		if id:
			try:
				instance = QuickRequest.objects.get(id=id)
			except QuickRequest.DoesNotExist, e:
				return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

			serializer = QuickRequestSerializer(instance=instance, data=request.data)
		else:
			serializer = QuickRequestSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
