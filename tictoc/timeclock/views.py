from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import FormView
from .forms import PunchInForm, PunchOutForm

from .models import Punch, Project

class ClockInOutView(FormView):

    def get_template_names(self):
        template_name = 'timeclock/home-clockin.html'
        records = self.request.user.punch_set.order_by('-time_in')
        if records:
            if records[0].is_clocked_in():
                template_name = 'timeclock/home-clockout.html'
        return template_name

    def get_form_class(self):
        records = self.request.user.punch_set.order_by('-time_in')
        if records:
            if records[0].is_clocked_in():
                return PunchOutForm
        return PunchInForm

    def get_context_data(self, **kwargs):
        context = super(ClockInOutView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if type(form).__name__ == 'PunchInForm':
            entry = Punch()
            entry.project = form.cleaned_data["project"]
            entry.user = self.request.user
            entry.save()
            return reverse('timeclock:ko')

        if type(form).__name__ == 'PunchOutForm':
            entry = self.request.user.punch_set.order_by('-time_in')[0]
            entry.note = form.cleaned_data["note"]
            entry.time_out = timezone.now()
            entry.save()
            return reverse('timeclock:ko')
