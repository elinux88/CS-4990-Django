from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
import datetime

class Stage(models.Model):
    name = models.CharField(max_length = 200)
    order = models.IntegerField(help_text = 'The order this is displayed on the screen')
    description = models.TextField(blank = True, null = True)
    value = models.IntegerField(help_text = 'On a scale of 0 to 100 of the stage of the pipeline')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        return reverse('crm:stage_detail', kwargs={'pk': self.pk})

class Company(models.Model):
    name = models.CharField(max_length = 200)
    website = models.URLField(max_length = 200, blank = True, null = True)
    address1 = models.CharField(max_length = 200, blank = True, null = True)
    address2 = models.CharField(max_length = 200, blank = True, null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    state = models.CharField(max_length = 200, blank = True, null = True)
    zipcode = models.CharField(max_length = 200, blank = True, null = True)
    country = models.CharField(max_length = 200, blank = True, null = True)
    phone = models.CharField(max_length = 200, blank = True, null = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'

    def get_absolute_url(self):
        return reverse('crm:company_detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    company = models.ForeignKey(Company, blank = True, null = True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    address1 = models.CharField(max_length = 200, blank = True, null = True)
    address2 = models.CharField(max_length = 200, blank = True, null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    state = models.CharField(max_length = 200, blank = True, null = True)
    zipcode = models.CharField(max_length = 200, blank = True, null = True)
    country = models.CharField(max_length = 200, blank = True, null = True)
    phone = models.CharField(max_length = 200, blank = True, null = True)
    email = models.EmailField(max_length = 200, blank = True, null = True)

    def get_full_name(self):
        return str(self.first_name) + " " + str(self.last_name)

    def __unicode__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('crm:contact_detail', kwargs={'pk': self.pk})

class Campaign(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crm:campaign_detail', kwargs={'pk': self.pk})

class Opportunity(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField()
    stage = models.ForeignKey(Stage)
    contact = models.ForeignKey(Contact)
    value = models.FloatField(help_text = 'How much this opportunity is worth to the organization')
    source = models.ForeignKey(Campaign, help_text = 'How did this contact find out about us?')
    user = models.ForeignKey(User, blank = True, null = True)
    create_date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'opportunities'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Opportunity, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('crm:opportunity_detail', kwargs={'pk': self.pk})

class CallLog(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateTimeField(auto_now_add = True)
    note = models.TextField()
    user = models.ForeignKey(User, blank = True, null = True)

    def __unicode__(self):
        return self.opportunity + " on " + self.date.strftime("%Y-%m-%d") + " by " + self.user.get_full_name()

    class Meta:
        ordering = ['-date', 'user']

    def get_absolute_url(self):
        return reverse('crm:calllog_detail', kwargs={'pk': self.pk})

class OpportunityStage(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    stage = models.ForeignKey(Stage)
    timestamp = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, blank = True, null = True)

    def __unicode__(self):
        return self.opportunity + " moved to " + self.stage

    def get_absolute_url(self):
        return reverse('crm:opportunity-stage_detail', kwargs={'pk': self.pk})

class Reminder(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateField()
    note = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

    def __unicode__(self):
        return self.opportunity + ": " + self.note

    def get_absolute_url(self):
        return reverse('crm:reminder_detail', kwargs={'pk': self.pk})

class Report(models.Model):
    name = models.CharField(max_length = 200)
    link = models.URLField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crm:report_detail', kwargs={'pk': self.pk})

