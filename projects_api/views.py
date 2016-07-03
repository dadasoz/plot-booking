from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView

from .serializers import ProjectsSerializer, PlotsSerializer, ProjectsForPlotsSerializer, PlotDetailsSerializer
from projects_api.models import Project, Plots

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class ProjectsList(APIView):

    """
    A GET endpoint that needs OAuth2 authentication
    """

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectsListForPlots(APIView):

    """
    A GET endpoint that needs OAuth2 authentication
    """

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectsForPlotsSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectsDetail(APIView):

    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectsSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlotList(APIView):

    """
    A GET endpoint that needs OAuth2 authentication
    """

    def get(self, request, format=None):
        plots = Plots.objects.all()
        serializer = PlotsSerializer(plots, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlotDetail(APIView):

    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Plots.objects.get(pk=pk)
        except Plots.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        plot = self.get_object(pk)
        serializer = PlotsSerializer(plot)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        plot = self.get_object(pk)
        serializer = PlotsSerializer(plot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        plot = self.get_object(pk)
        plot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlotWithProjectDetails(generics.RetrieveAPIView):
    serializer_class = PlotDetailsSerializer

    def get_object(self, project, plot_no):
        try:
            project = Project.objects.get(pk=project)
            return Plots.objects.get(plot_no=plot_no, project=project)
        except Plots.DoesNotExist:
            raise Http404

    def get(self, request, project, plot_no, format=None):
        plot = self.get_object(project, plot_no)
        serializer = PlotDetailsSerializer(plot)
        return Response(serializer.data)