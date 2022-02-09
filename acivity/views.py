from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from acivity.models import RecentActivity
from acivity.serializers import ActivitySerializer
# Create your views here.

class activityListView(APIView):
    def get(self, request, format=None):
        activity = RecentActivity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class activityDetails(APIView):
    def get(self, request, pk, format=None):
        activity = RecentActivity.objects.filter(title=pk)
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            activity = RecentActivity.objects.get(title=pk)
            serializer = ActivitySerializer(activity, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except RecentActivity.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delet(self, request, pk, format=None):
        try:
            activity = RecentActivity.objects.get(title=pk)
            activity.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RecentActivity.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)