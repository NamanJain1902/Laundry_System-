# Generated by Django 3.2.9 on 2021-11-23 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('employee_id', models.AutoField(help_text='Unique laundry num. for employee table', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mobile_num', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.gender')),
                ('hostels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.hostel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
