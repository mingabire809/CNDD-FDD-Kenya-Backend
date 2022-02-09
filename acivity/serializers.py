from acivity.models import RecentActivity
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentActivity
        fields = ['picture', 'title', 'date']