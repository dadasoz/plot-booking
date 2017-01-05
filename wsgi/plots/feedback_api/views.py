from feedback_api.models import Feedback
from feedback_api.serializers import FeedbackSerializer, FeedbackListSerializer, FeedbackDetailsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class FeedbackList(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FeedbackListSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateFeedback(generics.CreateAPIView):
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save()


class DestroyFeedback(generics.DestroyAPIView):
    serializer_class = FeedbackSerializer

    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        Feedback = self.get_object(pk)
        Feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FeedbackDetail(generics.RetrieveAPIView):
    serializer_class = FeedbackDetailsSerializer

    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Feedback = self.get_object(pk)
        serializer = FeedbackDetailsSerializer(Feedback)
        return Response(serializer.data)


class FeedbackUpdate(generics.UpdateAPIView):
    serializer_class = FeedbackSerializer
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        Feedback = self.get_object(pk)
        serializer = FeedbackSerializer(Feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
