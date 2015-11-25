from django.core.urlresolvers import reverse
from viewsets import ModelViewSet
from .models import CallLog, Stage, Company, Contact, Reminder, Opportunity, Campaign

class CallLogViewSet(ModelViewSet):
    model = CallLog
    exclude = ['user']
    fields = ['opportunity', 'note']

class StageViewSet(ModelViewSet):
    model = Stage

    def get_success_url(self):
        return reverse('crm:stage_index')

class CompanyViewSet(ModelViewSet):
    model = Company

class ContactViewSet(ModelViewSet):
    model = Contact

class ReminderViewSet(ModelViewSet):
    model = Reminder

class OpportunityViewSet(ModelViewSet):
    model = Opportunity
    exclude = ['user']
    fields = ['stage', 'company', 'contact', 'value', 'source']

class CampaignViewSet(ModelViewSet):
    model = Campaign

