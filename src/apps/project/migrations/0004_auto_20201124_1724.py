# Generated by Django 3.1.2 on 2020-11-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20201124_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='profile',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]
