# Generated by Django 3.1.7 on 2021-04-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msa_app', '0011_sales_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sales',
            name='sale_id',
            field=models.IntegerField(default=0),
        ),
    ]