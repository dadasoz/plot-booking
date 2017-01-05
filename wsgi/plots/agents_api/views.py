from agents_api.models import AgentsProfile
from agents_api.serializers import AgentSerializer, AgentListSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class AgentList(generics.ListAPIView):
    queryset = AgentsProfile.objects.all()
    serializer_class = AgentListSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = AgentListSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateAgent(generics.CreateAPIView):
    serializer_class = AgentSerializer

    def perform_create(self, serializer):
        serializer.save()


class DestroyAgent(generics.DestroyAPIView):
    serializer_class = AgentSerializer

    def get_object(self, pk):
        try:
            return AgentsProfile.objects.get(pk=pk)
        except AgentsProfile.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        agent = self.get_object(pk)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AgentDetail(generics.RetrieveAPIView):
    serializer_class = AgentSerializer

    def get_object(self, pk):
        try:
            return AgentsProfile.objects.get(pk=pk)
        except AgentsProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        agent = self.get_object(pk)
        serializer = AgentSerializer(agent)
        return Response(serializer.data)


class AgentUpdate(generics.UpdateAPIView):
    serializer_class = AgentSerializer
    def get_object(self, pk):
        try:
            return AgentsProfile.objects.get(pk=pk)
        except AgentsProfile.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        agent = self.get_object(pk)
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
