from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Pot
from .serializers import PotSerializer

# Requests made to /pots/
class PotListView(APIView):

    def get(self, _request):
      pots = Pot.objects.all()
      print('POTS ->', pots)
      serialized_pots = PotSerializer(pots, many=True)
      print('*** SERIALIZED POTS ***', serialized_pots.data)
      return Response(serialized_pots.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        pot = PotSerializer(data = request.data)
        if pot.is_valid():
            pot.save()
            return Response(pot.data, status=status.HTTP_201_CREATED)
        else:
            return Response(pot.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Requests made to /pots/pk/
class PotDetailView(APIView):

    def get(self, _request, pk):
        try:
            pot = Pot.objects.get(id=pk)
        except:
            return Response({'message': 'Pot not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized_pot = PotSerializer(pot)
        return Response(serialized_pot.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            pot = Pot.objects.get(id=pk)
            pot.delete()
        except:
              return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
      try:
          pot = Pot.objects.get(id=pk)
      except:
          return Response({'message': 'Pot not found'}, status=status.HTTP_404_NOT_FOUND)
      updated_pot = PotSerializer(pot, data=request.data)
      if updated_pot.is_valid():
          updated_pot.save()
          return Response(updated_pot.data, status=status.HTTP_202_ACCEPTED)
      else:
          return Response(updated_pot.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
