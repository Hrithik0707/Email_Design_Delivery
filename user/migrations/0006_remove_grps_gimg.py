# Generated by Django 2.2.6 on 2020-06-10 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200609_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grps',
            name='gimg',
        ),
    ]