#from django.conf.urls import patterns, url, include
#from .views import DashboardView, SearchResultsView, CallLogViewSet, CampaignViewSet, CompanyViewSet, ContactViewSet, OpportunityViewSet, ReminderViewSet, StageViewSet
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),

    url(r'^stage/$', views.StageView.as_view(), name='stage_index'),
    url(r'^stage/(?P<pk>\d+)/$', views.StageDetailView.as_view(), name='stage_detail'),
    url(r'^stage/create/$', views.StageCreateView.as_view(), name='stage_create'),
    url(r'^stage/(?P<pk>\d+)/update/$', views.StageUpdateView.as_view(), name='stage_update'),
    url(r'^stage/(?P<pk>\d+)/delete/$', views.StageDeleteView.as_view(), name='stage_delete'),

    url(r'^company/$', views.CompanyView.as_view(), name='company_index'),
    url(r'^company/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='company_detail'),
    url(r'^company/create/$', views.CompanyCreateView.as_view(), name='company_create'),
    url(r'^company/(?P<pk>\d+)/update/$', views.CompanyUpdateView.as_view(), name='company_update'),
    url(r'^company/(?P<pk>\d+)/delete/$', views.CompanyDeleteView.as_view(), name='company_delete'),

    url(r'^contact/$', views.ContactView.as_view(), name='contact_index'),
    url(r'^contact/(?P<pk>\d+)/$', views.ContactDetailView.as_view(), name='contact_detail'),
    url(r'^contact/create/$', views.ContactCreateView.as_view(), name='contact_create'),
    url(r'^contact/(?P<pk>\d+)/update/$', views.ContactUpdateView.as_view(), name='contact_update'),
    url(r'^contact/(?P<pk>\d+)/delete/$', views.ContactDeleteView.as_view(), name='contact_delete'),

    url(r'^campaign/$', views.CampaignView.as_view(), name='campaign_index'),
    url(r'^campaign/(?P<pk>\d+)/$', views.CampaignDetailView.as_view(), name='campaign_detail'),
    url(r'^campaign/create/$', views.CampaignCreateView.as_view(), name='campaign_create'),
    url(r'^campaign/(?P<pk>\d+)/update/$', views.CampaignUpdateView.as_view(), name='campaign_update'),
    url(r'^campaign/(?P<pk>\d+)/delete/$', views.CampaignDeleteView.as_view(), name='campaign_delete'),

    url(r'^opportunity/$', views.OpportunityView.as_view(), name='opportunity_index'),
    url(r'^opportunity/(?P<pk>\d+)/$', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    url(r'^opportunity/create/$', views.OpportunityCreateView.as_view(), name='opportunity_create'),
    url(r'^opportunity/(?P<pk>\d+)/update/$', views.OpportunityUpdateView.as_view(), name='opportunity_update'),
    url(r'^opportunity/(?P<pk>\d+)/delete/$', views.OpportunityDeleteView.as_view(), name='opportunity_delete'),

    url(r'^call-log/$', views.CallLogView.as_view(), name='call-log_index'),
    url(r'^call-log/(?P<pk>\d+)/$', views.CallLogDetailView.as_view(), name='call-log_detail'),
    url(r'^call-log/create/$', views.CallLogCreateView.as_view(), name='call-log_create'),
    url(r'^call-log/(?P<pk>\d+)/update/$', views.CallLogUpdateView.as_view(), name='call-log_update'),
    url(r'^call-log/(?P<pk>\d+)/delete/$', views.CallLogDeleteView.as_view(), name='call-log_delete'),

    url(r'^opportunity-stage/$', views.Opportunityopportunity-stageView.as_view(), name='opportunity-stage_index'),
    url(r'^opportunity-stage/(?P<pk>\d+)/$', views.Opportunityopportunity-stageDetailView.as_view(), name='opportunity-stage_detail'),
    url(r'^opportunity-stage/create/$', views.Opportunityopportunity-stageCreateView.as_view(), name='opportunity-stage_create'),
    url(r'^opportunity-stage/(?P<pk>\d+)/update/$', views.Opportunityopportunity-stageUpdateView.as_view(), name='opportunity-stage_update'),
    url(r'^opportunity-stage/(?P<pk>\d+)/delete/$', views.Opportunityopportunity-stageDeleteView.as_view(), name='opportunity-stage_delete'),

    url(r'^reminder/$', views.ReminderView.as_view(), name='reminder_index'),
    url(r'^reminder/(?P<pk>\d+)/$', views.ReminderDetailView.as_view(), name='reminder_detail'),
    url(r'^reminder/create/$', views.ReminderCreateView.as_view(), name='reminder_create'),
    url(r'^reminder/(?P<pk>\d+)/update/$', views.ReminderUpdateView.as_view(), name='reminder_update'),
    url(r'^reminder/(?P<pk>\d+)/delete/$', views.ReminderDeleteView.as_view(), name='reminder_delete'),

    url(r'^reports/$', TemplateView.as_view(template_name = 'report_list.html')),
]
#urlpatterns = patterns('',
#    url(r'^$', DashboardView.as_view(), name="dashboard"),
#    url(r'^search/$', SearchResultsView.as_view(), name="search"),
#    url('', include(CallLogViewSet().urls)),
#    url('', include(CampaignViewSet().urls)),
#    url('', include(CompanyViewSet().urls)),
#    url('', include(ContactViewSet().urls)),
#    url('', include(OpportunityViewSet().urls)),
#    url('', include(ReminderViewSet().urls)),
#    url('', include(StageViewSet().urls)),
#)
