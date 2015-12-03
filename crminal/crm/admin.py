from django.contrib import admin
from .models import CallLog, Campaign, Company, Contact, Opportunity, OpportunityStage, Reminder, Report, Stage

admin.site.register(CallLog)
admin.site.register(Campaign)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Opportunity)
admin.site.register(OpportunityStage)
admin.site.register(Reminder)
admin.site.register(Report)
admin.site.register(Stage)
