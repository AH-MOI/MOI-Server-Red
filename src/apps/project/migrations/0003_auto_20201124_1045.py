# Generated by Django 3.1.2 on 2020-11-24 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201124_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='closing_data',
            new_name='closing_date',
        ),
    ]
