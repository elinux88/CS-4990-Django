from django.conf.urls import url, include
from .views import CallLogViewSet, StageViewSet

urlpatterns = [
    url('', include(CallLogViewSet().urls)),
    url('', include(StageViewSet().urls)),
]
