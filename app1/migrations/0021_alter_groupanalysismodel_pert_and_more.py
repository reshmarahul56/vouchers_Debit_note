# Generated by Django 4.0.5 on 2022-09-22 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_alter_groupcreatemodel_comp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupanalysismodel',
            name='pert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group'),
        ),
        migrations.AlterField(
            model_name='purchasevouchermodel',
            name='udergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group'),
        ),
        migrations.AlterField(
            model_name='salevouchermodel',
            name='udergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group'),
        ),
        migrations.DeleteModel(
            name='groupcreatemodel',
        ),
    ]