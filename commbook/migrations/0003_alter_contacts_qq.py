# Generated by Django 3.2.7 on 2021-09-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commbook', '0002_alter_contacts_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='qq',
            field=models.BigIntegerField(null=True, verbose_name='QQ'),
        ),
    ]