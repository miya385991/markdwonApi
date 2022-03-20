from rest_framework import routers
from django.urls import path
from django.conf.urls import include
# from api.views import MarkDonwViewSet

router = routers.DefaultRouter()
# router.register('markdown', MarkDonwViewSet)

urlpatterns = [
    path('', include(router.urls)),
]