# Generated by Django 4.0.6 on 2022-10-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0062_rename_vou_type_voucher_sales_vou_type1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debit_Note',
            fields=[
                ('vou_type1', models.CharField(default=False, max_length=225)),
                ('pur_no', models.AutoField(default=True, primary_key=True, serialize=False)),
                ('invoiceno', models.IntegerField()),
                ('date', models.DateField(null=True)),
                ('party_AC_name', models.CharField(default=True, max_length=225)),
                ('Cur_bal', models.IntegerField(default=True)),
                ('purchaseledger', models.CharField(max_length=225)),
                ('Cur_bal1', models.IntegerField(default=True)),
                ('itemname', models.CharField(default=True, max_length=225)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('itemname1', models.CharField(default=True, max_length=225)),
                ('quantity1', models.IntegerField(null=True)),
                ('rate1', models.IntegerField(null=True)),
                ('amount1', models.IntegerField(null=True)),
                ('narration', models.CharField(default=True, max_length=225)),
                ('total_amount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='party_details',
        ),
        migrations.DeleteModel(
            name='receipt_details',
        ),
        migrations.DeleteModel(
            name='stock_item_allocat',
        ),
    ]