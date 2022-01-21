from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Pot
from .serializers import PotSerializer

# Create your views here.
class PotListView(APIView):

  def get(self, _request):
    pots = Pot.objects.all()
    print('POTS ->', pots)