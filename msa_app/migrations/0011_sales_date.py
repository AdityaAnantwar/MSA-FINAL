# Generated by Django 3.1.7 on 2021-04-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msa_app', '0010_remove_sales_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
