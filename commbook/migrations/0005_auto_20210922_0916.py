# Generated by Django 3.2.7 on 2021-09-22 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commbook', '0004_remove_contacts_gourp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comgroup',
            options={'ordering': ['-date_created'], 'verbose_name': '通讯录组', 'verbose_name_plural': '通讯录组'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['-date_created'], 'verbose_name': '联系人', 'verbose_name_plural': '联系人'},
        ),
    ]