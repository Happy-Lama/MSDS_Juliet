# Generated by Django 4.2.5 on 2023-09-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_merge_20230919_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceservice',
            name='total_cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='licenseservice',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cost',
            field=models.IntegerField(),
        ),
    ]
