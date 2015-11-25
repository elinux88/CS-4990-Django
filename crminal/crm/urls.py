from django.conf.urls import patterns, url, include
from .views import CallLogViewSet, StageViewSet, CompanyViewSet, ContactViewSet, ReminderViewSet, OpportunityViewSet, CampaignViewSet

urlpatterns = patterns('',
    url('', include(CallLogViewSet().urls)),
    url('', include(StageViewSet().urls)),
    url('', include(CompanyViewSet().urls)),
    url('', include(ContactViewSet().urls)),
    url('', include(ReminderViewSet().urls)),
    url('', include(OpportunityViewSet().urls)),
    url('', include(CampaignViewSet().urls)),
)
