from viewsets import ModelViewSet
from .models import CallLog, Stage

class CallLogViewSet(ModelViewSet):
    model = CallLog

class StageViewSet(ModelViewSet):
    model = Stage
