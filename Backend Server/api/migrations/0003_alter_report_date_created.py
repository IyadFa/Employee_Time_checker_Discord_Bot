# Generated by Django 4.0.3 on 2022-04-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_weeklyreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
