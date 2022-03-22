from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from api.views import MarkdownViewSet

router = routers.DefaultRouter()
router.register('markdown', MarkdownViewSet)

urlpatterns = [
    path('', include(router.urls)),
]