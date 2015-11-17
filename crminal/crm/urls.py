from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name="main"),

    # CallLog
    url(r'^call-log/$', login_required(views.CallLogListView.as_view()), name="call-log_index"),
    url(r'^call-log/(?P<pk>\d+)/$', login_required(views.CallLogDetailView.as_view()), name="call-log_detail"),
    url(r'^call-log/create/$', login_required(views.CallLogCreateView.as_view()), name="call-log_create"),
    url(r'^call-log/(?P<pk>\d+)/delete/$', login_required(views.CallLogDeleteView.as_view()), name="call-log_delete"),

    # Stage
    url(r'^stage/$', login_required(views.StageListView.as_view()), name="stage_index"),
    url(r'^stage/(?P<pk>\d+)/$', login_required(views.StageDetailView.as_view()), name="stage_detail"),
    url(r'^stage/create/$', login_required(views.StageCreateView.as_view()), name="stage_create"),
    url(r'^stage/(?P<pk>\d+)/update/$', login_required(views.StageUpdateView.as_view()), name="stage_update"),
    url(r'^stage/(?P<pk>\d+)/delete/$', login_required(views.StageDeleteView.as_view()), name="stage_delete"),

    # Company
    url(r'^company/(?P<pk>\d+)/$', login_required(views.CompanyDetailView.as_view()), name="company_detail"),

    # Contact
    url(r'^contact/(?P<pk>\d+)/$', login_required(views.ContactDetailView.as_view()), name="contact_detail"),

    # Reminder
    url(r'^reminder/(?P<pk>\d+)/$', login_required(views.ReminderDetailView.as_view()), name="reminder_detail"),

    # Opportunity
    url(r'^opportunity/(?P<pk>\d+)/$', login_required(views.OpportunityDetailView.as_view()), name="opportunity_detail"),

    # Campaign
    url(r'^campaign/(?P<pk>\d+)/$', login_required(views.CampaignDetailView.as_view()), name="campaign_detail"),
]
