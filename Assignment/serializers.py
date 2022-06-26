from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('__all__')
            
class ParagraphsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Paragraphs
            fields = ('__all__')