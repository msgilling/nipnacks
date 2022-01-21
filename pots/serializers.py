from rest_framework import serializers
from .models import Pot

class PotSerializer(serializers.ModelSerializer):
    class Meta:
      model = Pot
      fields = '__all__'