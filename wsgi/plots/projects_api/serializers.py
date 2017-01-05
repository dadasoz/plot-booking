from rest_framework import serializers
from projects_api.models import Project, Plots
import datetime


class ProjectsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    description = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    village = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    taluka = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    district = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    state = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    area = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    plot_no = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    gat_no = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    survey_no = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    is_active = serializers.BooleanField(required=False)
    created_at = serializers.DateTimeField(
        required=False, format="%Y-%m-%dT%H:%M:%S")
    updated_at = serializers.DateTimeField(
        required=False, initial=datetime.date.today, format="%Y-%m-%dT%H:%M:%S")
    start_date = serializers.CharField(required=False)
    date_closed = serializers.CharField(required=False)
    rate_per_sqft = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

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
        instance.start_date = validated_data.get(
            'start_date', instance.start_date)
        instance.survey_no = validated_data.get(
            'survey_no', instance.survey_no)
        instance.rate_per_sqft = validated_data.get(
            'rate_per_sqft', instance.rate_per_sqft)
        instance.taluka = validated_data.get('taluka', instance.taluka)
        instance.district = validated_data.get('district', instance.district)
        instance.state = validated_data.get('state', instance.state)
        instance.village = validated_data.get('village', instance.village)
        instance.save()
        return instance


class PlotsSerializer(serializers.ModelSerializer):

    project_name = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = Plots
        fields = ('pk', 'plot_no', 'is_booked', 'is_saled', 'facing', 'width',
                  'breadth', 'area', 'created_at', 'basic_cost', 'project', 'project_name', 'rate_per_sqft', 'survey_no')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Plots.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.plot_no = validated_data.get('plot_no', instance.plot_no)
        instance.basic_cost = validated_data.get(
            'basic_cost', instance.basic_cost)
        instance.is_booked = validated_data.get(
            'is_booked', instance.is_booked)
        instance.is_saled = validated_data.get('is_saled', instance.is_saled)
        instance.facing = validated_data.get('facing', instance.facing)
        instance.width = validated_data.get('width', instance.width)
        instance.breadth = validated_data.get('breadth', instance.breadth)
        instance.area = validated_data.get('area', instance.area)
        instance.survey_no = validated_data.get(
            'survey_no', instance.survey_no)
        instance.rate_per_sqft = validated_data.get(
            'rate_per_sqft', instance.rate_per_sqft)
        instance.save()
        return instance


class ProjectsForPlotsSerializer(serializers.ModelSerializer):

    project_name = serializers.CharField(source='name', read_only=True)

    class Meta:
        model = Project
        fields = ('pk', 'project_name')


class PlotDetailsSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = Plots
        fields = ('pk', 'plot_no', 'is_booked', 'is_saled', 'facing', 'width',
                  'breadth', 'area', 'created_at', 'basic_cost', 'project', 'rate_per_sqft', 'survey_no', 'project_name')
