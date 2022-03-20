from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import MarkdownImageSerializer
from .models import MarkdownImage

class MMarkdownViewSet(viewsets.ModelViewSet):
    queryset = MarkdownImage.objects.all()
    serializer_class = MarkdownImageSerializer

    def post(self, request, *args, **kwargs):
        img = request.data['img']
        title = request.data['title']
        MarkdownImage.objects.create(title=title, img=img)
        return HttpResponse({'message':'New markdownImage created'},status=200)