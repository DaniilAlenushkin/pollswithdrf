from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from . import models, serializers


class PollList(APIView):
    def get(self, request):
        polls = models.Poll.objects.all()
        data = serializers.PollSerializer(polls, many=True).data
        return Response(data)


class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(models.Poll, pk=pk)
        data = serializers.PollSerializer(poll).data
        return Response(data)
