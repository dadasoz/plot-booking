from rest_framework import serializers
from agents_api.models import AgentsProfile


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentsProfile


class AgentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentsProfile
        fields = ('pk', 'full_name', 'email', 'mobile',
                  'alternate_mobile', 'address1')


class AgentDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentsProfile
