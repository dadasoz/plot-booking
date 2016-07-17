from rest_framework import serializers
from feedback_api.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = Feedback


class FeedbackListSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = Feedback


class FeedbackDetailsSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = Feedback
