from rest_framework import serializers

from ..models import Food


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
