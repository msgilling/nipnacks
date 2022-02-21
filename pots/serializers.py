from rest_framework import serializers
from .models import Pot
from comments.serializers import CommentSerializer

class PotSerializer(serializers.ModelSerializer):
    class Meta:
      model = Pot
      fields = '__all__'



class PopulatedPotSerializer(PotSerializer):

    
    comment_set = CommentSerializer(read_only=True, many=True)