# Generated by Django 2.2.6 on 2020-06-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200609_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grps',
            name='contacts',
        ),
        migrations.AddField(
            model_name='grps',
            name='contacts',
            field=models.ManyToManyField(to='user.Contacts'),
        ),
    ]