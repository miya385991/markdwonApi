from rest_framework import serializers
from .models import MarkdownImage

class MarkdownImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkdownImage
        fields = ['id', 'title', 'img']