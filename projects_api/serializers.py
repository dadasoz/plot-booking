from rest_framework import serializers
from projects_api.models import Project


class ProjectsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    area = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    plot_no = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    gat_no = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    is_active = serializers.BooleanField(required=False)
    created_at = serializers.DateField(required=False)
    updated_at = serializers.DateField(required=False)
    start_date = serializers.DateField(required=False)
    date_closed = serializers.DateField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.area = validated_data.get('area', instance.area)
        instance.plot_no = validated_data.get('plot_no', instance.plot_no)
        instance.gat_no = validated_data.get('gat_no', instance.gat_no)
        instance.save()
        return instance
