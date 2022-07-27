from rest_framework import serializers
from mainapp.models import HexData, Hypothesis, Profile


class HexDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HexData
        fields = ['source', 'from_number', 'to_number', 'hexdatastring']


class HypothesisSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Hypothesis
        fields = ['name', 'created_date', 'user']


class HypothesisCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hypothesis
        fields = ['name', 'description', 'lat_long_field']

    def create(self, validated_data):
        user = self.context['request'].user
        hypothesis = Hypothesis.objects.create(user=user, **validated_data)
        return hypothesis


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'birth_date', 'address', 'user_id']
