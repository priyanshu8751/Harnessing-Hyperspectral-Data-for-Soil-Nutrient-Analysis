import datetime as dt

from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.models import RawPayload, Data, DaySummary
from . import serializers, filters


class DataPostViewset(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = RawPayload.objects.none()
    serializer_class = serializers.RawPayloadSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        req_data = request.data
        print(req_data)
        data = req_data
        if 'payload' in req_data:
            data = req_data.get('payload')

        if data == "":
            return Response({
                'success': False,
                'message': 'Some issue in data!'
            })

        validated_data = {
            "payload": data
        }
        serializer = self.get_serializer()
        instance = serializer.create(validated_data)
        instance.save()
        return Response({
            'success': True,
            'message': 'Raw payload saved!'
        })


class DataViewset(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = serializers.DataSerializer
    filterset_class = filters.DataFilters


class DaySummaryViewset(viewsets.ModelViewSet):
    queryset = DaySummary.objects.all()
    serializer_class = serializers.DaySummarySerializer
    filterset_class = filters.DaySummaryFilters
