from rest_framework import serializers
from .models import Markdown

class MarkdownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Markdown
        fields = ['id', 'title', 'overview', 'category', 'author',  'created', 'updated', 'text']