# Generated by Django 3.2.5 on 2021-08-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_facts_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='facts',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
