from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import MarkdownSerializer
from .models import Markdown


class MarkdownViewSet(viewsets.ModelViewSet):
    queryset = Markdown.objects.all()
    serializer_class = MarkdownSerializer

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        overview = request.data['overview']
        category = request.data['category']
        author = request.data['author']
        # img = request.data['img']
        text = request.data['text']


        Markdown.objects.create(
            title=title, overview=overview, category=category,
            author=author, text=text
        )
        return HttpResponse(
            {'message': 'New markdown created'}, status=200)
