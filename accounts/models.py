from django.db import models

# Create your models here.

class Account(models.Model):
    
    # Auto increment id : default
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    address_line = models.CharField(max_length=40, blank=True, null=True)
    address_state = models.CharField(max_length=40, blank=True, null=True)
    address_city = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name_plural = 'Account'