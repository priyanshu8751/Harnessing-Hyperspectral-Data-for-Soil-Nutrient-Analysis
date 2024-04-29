from rest_framework import serializers

class ModelOutputSerializer(serializers.Serializer):
    band_value = serializers.ListField(child=serializers.FloatField())
    model_output = serializers.ListField(child=serializers.FloatField())
