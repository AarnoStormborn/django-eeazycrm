# Generated by Django 4.1.4 on 2022-12-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealstage',
            name='close_type',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]