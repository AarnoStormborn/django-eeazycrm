from django.db import models

class LeadStage(models.Model):

    status_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"Lead Stage: {self.status_name}"

    class Meta:
        verbose_name_plural = 'Lead Stage'

class LeadSource(models.Model):

    source_name = models.CharField(max_length=40)

    def __str__(self):
        return f"Lead Source: {self.source_name}"

    class Meta:
        verbose_name_plural = 'Lead Source'

class Lead(models.Model):
    
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=40)
    email = models.CharField(max_length=120, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address_line = models.CharField(max_length=40, blank=True, null=True)
    address_state = models.CharField(max_length=40, blank=True, null=True)
    address_city = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40)
    lead_stage_id = models.ForeignKey(LeadStage, on_delete=models.SET_NULL, null=True)
    lead_source_id = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=200, blank=True, null=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='leads', blank=True, null=True)

    def __str__(self):
        return f"{self.title} Source: {self.lead_source_id.source_name}"

    class Meta:
        verbose_name_plural = 'Lead'