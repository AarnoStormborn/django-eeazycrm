# Generated by Django 4.1.4 on 2022-12-08 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_remove_account_upload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=120, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('address_line', models.CharField(blank=True, max_length=40, null=True)),
                ('address_state', models.CharField(blank=True, max_length=40, null=True)),
                ('address_city', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(max_length=40)),
                ('notes', models.TextField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
