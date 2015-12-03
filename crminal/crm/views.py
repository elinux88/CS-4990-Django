from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.views.generic import TemplateView, UpdateView
from viewsets import ModelViewSet
from .models import CallLog, Campaign, Company, Contact, Opportunity, Reminder, Stage

class DashboardView(TemplateView):
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['opportunity_list'] = Opportunity.objects.all().order_by('-create_date')[:5]
        context['reminder_list'] = Reminder.objects.all().exclude(completed = True).order_by('date')[:5]
        context['stage_list'] = User.objects.annotate(num_opp = Count('opportunity'))
        context['stage_by_opp_list'] = Stage.objects.annotate(opp_count = Count('opportunity'))

        return context

class CallLogViewSet(ModelViewSet):
    model = CallLog
    exclude = ['user']
    fields = ['opportunity', 'note']

class CampaignViewSet(ModelViewSet):
    model = Campaign

class CompanyViewSet(ModelViewSet):
    model = Company

class ContactViewSet(ModelViewSet):
    model = Contact

class OpportunityViewSet(ModelViewSet):
    model = Opportunity
    exclude = ['user']
    fields = ['stage', 'company', 'contact', 'value', 'source']

class ReminderViewSet(ModelViewSet):
    model = Reminder

class StageViewSet(ModelViewSet):
    model = Stage

