from django.contrib import admin
from .models import *

admin.site.register(LeadSource)
admin.site.register(LeadStage)
admin.site.register(Lead)