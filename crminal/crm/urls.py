from django.conf.urls import patterns, url, include
from .views import DashboardView, CallLogViewSet, CampaignViewSet, CompanyViewSet, ContactViewSet, OpportunityViewSet, ReminderViewSet, StageViewSet

urlpatterns = patterns('',
    url(r'^$', DashboardView.as_view(), name="dashboard"),
    url('', include(CallLogViewSet().urls)),
    url('', include(CampaignViewSet().urls)),
    url('', include(CompanyViewSet().urls)),
    url('', include(ContactViewSet().urls)),
    url('', include(OpportunityViewSet().urls)),
    url('', include(ReminderViewSet().urls)),
    url('', include(StageViewSet().urls)),
)
