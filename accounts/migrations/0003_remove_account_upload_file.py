# Generated by Django 4.1.4 on 2022-12-08 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_options_alter_account_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='upload_file',
        ),
    ]