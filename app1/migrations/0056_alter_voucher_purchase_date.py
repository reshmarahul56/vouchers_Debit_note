# Generated by Django 4.0.6 on 2022-10-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0055_alter_voucher_purchase_itemname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher_purchase',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
