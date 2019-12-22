from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Link
from .serializers import LinkSerializer
# Create your views here.

class LinkView(APIView):
    def get(self, request):
        links = Link.objects.all()
        serializer = LinkSerializer(links)
        return Response({'domains': serializer.data})