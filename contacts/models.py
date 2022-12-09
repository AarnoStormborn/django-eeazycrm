from django.db import models
from accounts.models import Account

class Contact(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=120, unique=True)
    # avatar = models.CharField(max_length=25)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address_line = models.CharField(max_length=40, blank=True, null=True)
    address_state = models.CharField(max_length=40, blank=True, null=True)
    address_city = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40)
    notes = models.TextField(max_length=200, blank=True, null=True) 
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Contact'

