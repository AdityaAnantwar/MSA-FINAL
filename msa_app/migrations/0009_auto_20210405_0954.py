# Generated by Django 3.1.7 on 2021-04-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msa_app', '0008_stock_vendor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='threshold',
        ),
        migrations.AddField(
            model_name='sales',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
