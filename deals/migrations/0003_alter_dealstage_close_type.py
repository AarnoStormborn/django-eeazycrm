# Generated by Django 4.1.4 on 2022-12-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_alter_dealstage_close_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealstage',
            name='close_type',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
