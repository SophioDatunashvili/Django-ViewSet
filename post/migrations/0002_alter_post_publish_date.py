# Generated by Django 4.1.5 on 2023-02-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]