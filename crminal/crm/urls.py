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
   url(r'^stage/delete/success/$', TemplateView.as_view(template_name="crm/stage_delete_success.html"), name="stagedeletesuccess"),

    url(r'^company/$', views.CompanyView.as_view(), name='company_index'),
    url(r'^company/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='company_detail'),
    url(r'^company/create/$', views.CompanyCreateView.as_view(), name='company_create'),
    url(r'^company/(?P<pk>\d+)/update/$', views.CompanyUpdateView.as_view(), name='company_update'),
    url(r'^company/(?P<pk>\d+)/delete/$', views.CompanyDeleteView.as_view(), name='company_delete'),
   url(r'^company/delete/success/$', TemplateView.as_view(template_name="crm/company_delete_success.html"), name="companydeletesuccess"),

    url(r'^contact/$', views.ContactView.as_view(), name='contact_index'),
    url(r'^contact/(?P<pk>\d+)/$', views.ContactDetailView.as_view(), name='contact_detail'),
    url(r'^contact/create/$', views.ContactCreateView.as_view(), name='contact_create'),
    url(r'^contact/(?P<pk>\d+)/update/$', views.ContactUpdateView.as_view(), name='contact_update'),
    url(r'^contact/(?P<pk>\d+)/delete/$', views.ContactDeleteView.as_view(), name='contact_delete'),
   url(r'^contact/delete/success/$', TemplateView.as_view(template_name="crm/contact_delete_success.html"), name="contactdeletesuccess"),

    url(r'^campaign/$', views.CampaignView.as_view(), name='campaign_index'),
    url(r'^campaign/(?P<pk>\d+)/$', views.CampaignDetailView.as_view(), name='campaign_detail'),
    url(r'^campaign/create/$', views.CampaignCreateView.as_view(), name='campaign_create'),
    url(r'^campaign/(?P<pk>\d+)/update/$', views.CampaignUpdateView.as_view(), name='campaign_update'),
    url(r'^campaign/(?P<pk>\d+)/delete/$', views.CampaignDeleteView.as_view(), name='campaign_delete'),
   url(r'^campaign/delete/success/$', TemplateView.as_view(template_name="crm/campaign_delete_success.html"), name="campaigndeletesuccess"),

    url(r'^opportunity/$', views.OpportunityView.as_view(), name='opportunity_index'),
    url(r'^opportunity/(?P<pk>\d+)/$', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    url(r'^opportunity/create/$', views.OpportunityCreateView.as_view(), name='opportunity_create'),
    url(r'^opportunity/(?P<pk>\d+)/update/$', views.OpportunityUpdateView.as_view(), name='opportunity_update'),
    url(r'^opportunity/(?P<pk>\d+)/delete/$', views.OpportunityDeleteView.as_view(), name='opportunity_delete'),
   url(r'^opportunity/delete/success/$', TemplateView.as_view(template_name="crm/opportunity_delete_success.html"), name="opportunitydeletesuccess"),

    url(r'^calllog/$', views.CallLogView.as_view(), name='calllog_index'),
    url(r'^calllog/(?P<pk>\d+)/$', views.CallLogDetailView.as_view(), name='calllog_detail'),
    url(r'^calllog/create/$', views.CallLogCreateView.as_view(), name='calllog_create'),
    url(r'^calllog/(?P<pk>\d+)/update/$', views.CallLogUpdateView.as_view(), name='calllog_update'),
    url(r'^calllog/(?P<pk>\d+)/delete/$', views.CallLogDeleteView.as_view(), name='calllog_delete'),
   url(r'^calllog/delete/success/$', TemplateView.as_view(template_name="crm/calllog_delete_success.html"), name="calllogdeletesuccess"),

    url(r'^reminder/$', views.ReminderView.as_view(), name='reminder_index'),
    url(r'^reminder/(?P<pk>\d+)/$', views.ReminderDetailView.as_view(), name='reminder_detail'),
    url(r'^reminder/create/$', views.ReminderCreateView.as_view(), name='reminder_create'),
    url(r'^reminder/(?P<pk>\d+)/update/$', views.ReminderUpdateView.as_view(), name='reminder_update'),
    url(r'^reminder/(?P<pk>\d+)/delete/$', views.ReminderDeleteView.as_view(), name='reminder_delete'),
   url(r'^reminder/delete/success/$', TemplateView.as_view(template_name="crm/reminder_delete_success.html"), name="reminderdeletesuccess"),

    url(r'^report/$', views.ReportView.as_view(), name='report_index'),
    url(r'^report/(?P<pk>\d+)/$', views.ReportDetailView.as_view(), name='report_detail'),
    url(r'^report/create/$', views.ReportCreateView.as_view(), name='report_create'),
    url(r'^report/(?P<pk>\d+)/update/$', views.ReportUpdateView.as_view(), name='report_update'),
    url(r'^report/(?P<pk>\d+)/delete/$', views.ReportDeleteView.as_view(), name='report_delete'),
   url(r'^report/delete/success/$', TemplateView.as_view(template_name="crm/report_delete_success.html"), name="reportdeletesuccess"),

    url(r'^search/$', views.SearchResultsView.as_view(), name='search'),
]
