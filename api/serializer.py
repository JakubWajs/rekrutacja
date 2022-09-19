from rest_framework.serializers import ModelSerializer

from api.models import Link


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['source_link', 'short_link']
