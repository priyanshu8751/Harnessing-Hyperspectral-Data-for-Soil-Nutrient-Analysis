from datetime import datetime
from django.utils import timezone

from rest_framework import serializers

from base.models import RawPayload, Data, DaySummary


class RawPayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawPayload
        fields = ('payload',)

    def create(self, validated_data):
        payload = validated_data['payload']

        def extract_value(key):
            key_start = payload.find(key) + len(key) + 1
            key_end = payload.find('&', key_start)
            if key_end == -1:
                value = payload[key_start:]
            else:
                value = payload[key_start:key_end]
            return value

        api_key = extract_value('api_key')

        timestamp = datetime.now()
        raw_payload = RawPayload(timestamp=timestamp, payload=payload)
        return raw_payload


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class DaySummarySerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name', read_only=True)

    class Meta:
        model = DaySummary
        fields = ('device', 'device_name', 'date', 'param', 'value')
        read_only_fields = [f.name for f in DaySummary._meta.get_fields()]
