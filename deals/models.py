from django.db import models
from accounts.models import Account
from contacts.models import Contact

class DealStage(models.Model):

    stage_name = models.CharField(max_length=20)
    display_order = models.IntegerField()
    close_type = models.CharField(max_length=10, null=True, blank=True, default=None)

    def __str__(self):
        return f"Deal Stage: {self.stage_name}"

    class Meta:
        verbose_name_plural = 'Deal Stage'

class Deal(models.Model):
    
    title = models.CharField(max_length=100)
    expected_close_price = models.DecimalField(max_digits= 10,decimal_places=2)
    expected_close_date = models.DateField(auto_now_add=False, blank=True, null=True)
    deal_stage_id = models.ForeignKey(DealStage, on_delete=models.SET_NULL, null=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='deal')
    contact_id = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=200, blank=True, null=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='deals', blank=True, null=True)

    def __str__(self):
        return f"Deal {self.title} Account: {self.account_id.name}"

    class Meta:
        verbose_name_plural = 'Deal'

