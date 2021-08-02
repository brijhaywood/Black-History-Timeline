from rest_framework import serializers
from .models import Facts

class FactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facts
        fields = ('title', 'year', 'description', 'category')