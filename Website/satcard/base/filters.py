from django_filters import rest_framework as filters

from base.models import Data, DaySummary


COMPARE_FILTERS = ['lte', 'gte', 'lt', 'gt', 'exact']
APPROX_MATCH_FILTERS = ['exact', 'startswith', 'contains', 'in']
MATCH_FILTERS = ['exact', 'in']


class DataFilters(filters.FilterSet):
    class Meta:
        model = Data
        fields = {
            'device_id': MATCH_FILTERS,
            'timestamp': COMPARE_FILTERS
        }


class DaySummaryFilters(filters.FilterSet):
    class Meta:
        model = DaySummary
        fields = {
            'device_id': MATCH_FILTERS,
            'date': COMPARE_FILTERS,
            'param': MATCH_FILTERS
        }
