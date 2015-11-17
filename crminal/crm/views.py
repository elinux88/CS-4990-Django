from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CallLog, Stage, Company, Contact, Reminder, Opportunity, Campaign

class MainView(TemplateView):
    template_name = 'base.html'

# CallLog

class CallLogListView(ListView):
    model = CallLog
    paginate_by = 10

    def get_queryset(self):
        return CallLog.objects.order_by('-date')

class CallLogDetailView(DetailView):
    model = CallLog

class CallLogCreateView(CreateView):
    model = CallLog
    fields = ['opportunity', 'note']

    def get_success_url(self):
        return reverse('crm:call-log_index')

    def form_valid(self, form):
        u = form.save(commit=False)
        u.user = User.objects.filter(user=self.request.user)[0]
        u.save()
        return super(CallLogCreateView, self).form_valid(form)

class CallLogDeleteView(DeleteView):
    model = CallLog

# Stage

class StageListView(ListView):
    model = Stage
    paginate_by = 10

    def get_queryset(self):
        return Stage.objects.order_by('order')

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

# Company

class CompanyDetailView(DetailView):
    model = Company

# Contact

class ContactDetailView(DetailView):
    model = Contact

# Reminder

class ReminderDetailView(DetailView):
    model = Reminder

# Opportunity

class OpportunityDetailView(DetailView):
    model = Opportunity

# Campaign

class CampaignDetailView(DetailView):
    model = Campaign

