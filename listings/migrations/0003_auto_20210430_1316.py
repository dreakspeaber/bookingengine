# Generated by Django 3.2 on 2021-04-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_blockeddays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockeddays',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blockeddays',
            name='start_date',
            field=models.DateField(),
        ),
    ]