# Generated by Django 4.0.4 on 2022-09-30 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_cost_centre_status_create_employeegroup_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_employeegroup',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]