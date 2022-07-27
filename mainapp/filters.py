from django_filters.rest_framework import FilterSet
from .models import HexData


class HexDataFilter(FilterSet):
    class Meta:
        model = HexData
        fields = {
            'created_date': ['gte', 'lte']
        }
