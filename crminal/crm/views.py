from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

# Stage

class StageView(ListView):
    model = Stage

class StageDetailView(DetailView):
    model = Stage

class StageCreateView(CreateView):
    model = Stage

class StageUpdateView(UpdateView):
    model = Stage

class StageDeleteView(DeleteView):
    model = Stage

# Company

class CompanyView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company

class CompanyUpdateView(UpdateView):
    model = Company

class CompanyDeleteView(DeleteView):
    model = Company

# Contact

class ContactView(ListView):
    model = Contact

class ContactDetailView(DetailView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact

class ContactDeleteView(DeleteView):
    model = Contact

# Campaign

class CampaignView(ListView):
    model = Campaign

class CampaignDetailView(DetailView):
    model = Campaign

class CampaignCreateView(CreateView):
    model = Campaign

class CampaignUpdateView(UpdateView):
    model = Campaign

class CampaignDeleteView(DeleteView):
    model = Campaign

# Opportunity

class OpportunityView(ListView):
    model = Opportunity

class OpportunityDetailView(DetailView):
    model = Opportunity

class OpportunityCreateView(CreateView):
    model = Opportunity

class OpportunityUpdateView(UpdateView):
    model = Opportunity

class OpportunityDeleteView(DeleteView):
    model = Opportunity

# CallLog

class CallLogView(ListView):
    model = CallLog

class CallLogDetailView(DetailView):
    model = CallLog

class CallLogCreateView(CreateView):
    model = CallLog

class CallLogUpdateView(UpdateView):
    model = CallLog

class CallLogDeleteView(DeleteView):
    model = CallLog

# OpportunityStage

class OpportunityStageView(ListView):
    model = OpportunityStage

class OpportunityStageDetailView(DetailView):
    model = OpportunityStage

class OpportunityStageCreateView(CreateView):
    model = OpportunityStage

class OpportunityStageUpdateView(UpdateView):
    model = OpportunityStage

class OpportunityStageDeleteView(DeleteView):
    model = OpportunityStage

# Reminder

class ReminderView(ListView):
    model = Reminder

class ReminderDetailView(DetailView):
    model = Reminder

class ReminderCreateView(CreateView):
    model = Reminder

class ReminderUpdateView(UpdateView):
    model = Reminder

class ReminderDeleteView(DeleteView):
    model = Reminder



class SearchResultsView(TemplateView):
    template_name = 'crm/search_results.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)

        if not self.request.GET.get('q', None):
            return context

        term = self.request.GET['q']
        context['searchterm'] = term
        context['opportunity_list'] = Opportunity.objects.filter(name_icontains = term)

        return context

#class CallLogViewSet(ModelViewSet):
#    model = CallLog
#    exclude = ['user']
#    fields = ['opportunity', 'note']

#class CampaignViewSet(ModelViewSet):
#    model = Campaign

#class CompanyViewSet(ModelViewSet):
#    model = Company

#class ContactViewSet(ModelViewSet):
#    model = Contact

#class OpportunityViewSet(ModelViewSet):
#    model = Opportunity
#    exclude = ['user']
#    fields = ['stage', 'company', 'contact', 'value', 'source']

#class ReminderViewSet(ModelViewSet):
#    model = Reminder

#class StageViewSet(ModelViewSet):
#    model = Stage

