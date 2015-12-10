from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stage, Company, Contact, Campaign, Opportunity, CallLog, OpportunityStage, Reminder, Report

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
    fields = ['name', 'order', 'description', 'value']

class StageUpdateView(UpdateView):
    model = Stage
    fields = ['name', 'order', 'description', 'value']

class StageDeleteView(DeleteView):
    model = Stage
    success_url = reverse_lazy('crm:stagedeletesuccess')

# Company

class CompanyView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('crm:companydeletesuccess')

# Contact

class ContactView(ListView):
    model = Contact

class ContactDetailView(DetailView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    fields = ['company', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone', 'email']

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['company', 'first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone', 'email']

class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('crm:contactdeletesuccess')

# Campaign

class CampaignView(ListView):
    model = Campaign

class CampaignDetailView(DetailView):
    model = Campaign

class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['name', 'description']

class CampaignUpdateView(UpdateView):
    model = Campaign
    fields = ['name', 'description']

class CampaignDeleteView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('crm:campaigndeletesuccess')

# Opportunity

class OpportunityView(ListView):
    model = Opportunity

class OpportunityDetailView(DetailView):
    model = Opportunity

class OpportunityCreateView(CreateView):
    model = Opportunity
    fields = ['name', 'stage', 'contact', 'value', 'source']

class OpportunityUpdateView(UpdateView):
    model = Opportunity
    fields = ['name', 'stage', 'contact', 'value', 'source']

    def form_valid(self, form):
        opportunity = form.save(commit=False)
        if opportunity.stage.value > self.get_object().stage.value:
            opp_stage = OpportunityStage()
            opp_stage.opportunity = Opportunity.objects.all().filter(id = self.get_object().pk)[0]
            opp_stage.stage = form.cleaned_data['stage']
            #opp_stage.user = self.request.user
            opp_stage.save()
        opportunity.save()
        return super(OpportunityUpdateView, self).form_valid(form)

class OpportunityDeleteView(DeleteView):
    model = Opportunity
    success_url = reverse_lazy('crm:opportunitydeletesuccess')

# CallLog

class CallLogView(ListView):
    model = CallLog

class CallLogDetailView(DetailView):
    model = CallLog

class CallLogCreateView(CreateView):
    model = CallLog
    fields = ['opportunity', 'note']

class CallLogUpdateView(UpdateView):
    model = CallLog
    fields = ['opportunity', 'note']

class CallLogDeleteView(DeleteView):
    model = CallLog
    success_url = reverse_lazy('crm:calllogdeletesuccess')

# Reminder

class ReminderView(ListView):
    model = Reminder

class ReminderDetailView(DetailView):
    model = Reminder

class ReminderCreateView(CreateView):
    model = Reminder
    fields = ['opportunity', 'date', 'note', 'completed']

class ReminderUpdateView(UpdateView):
    model = Reminder
    fields = ['opportunity', 'date', 'note', 'completed']

class ReminderDeleteView(DeleteView):
    model = Reminder
    success_url = reverse_lazy('crm:reminderdeletesuccess')

# Report

class ReportView(ListView):
    model = Report

class ReportDetailView(DetailView):
    model = Report

class ReportCreateView(CreateView):
    model = Report
    fields = ['name', 'link']

class ReportUpdateView(UpdateView):
    model = Report
    fields = ['name', 'link']

class ReportDeleteView(DeleteView):
    model = Report
    success_url = reverse_lazy('crm:reportdeletesuccess')



class SearchResultsView(TemplateView):
    template_name = 'crm/search_results.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)

        if not self.request.GET.get("q", None):
            return context

        term = self.request.GET["q"]
        context['searchterm'] = term
        context['opportunity_list'] = Opportunity.objects.filter(name__icontains = term)
        context['contact_list'] = Contact.objects.filter(first_name__icontains = term)
        context['company_list'] = Company.objects.filter(name__icontains = term)
        context['calllog_list'] = CallLog.objects.filter(note__icontains = term)

        return context

