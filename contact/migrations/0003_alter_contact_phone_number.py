# Generated by Django 4.0.6 on 2022-07-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_coutry_code_contact_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
