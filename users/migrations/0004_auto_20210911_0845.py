# Generated by Django 2.2.10 on 2021-09-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210911_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.BigIntegerField(blank=True, max_length=11, null=True, verbose_name='电话'),
        ),
    ]
