# Generated by Django 3.1.3 on 2023-08-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0008_donation_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationarea',
            name='areaname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donationarea',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
