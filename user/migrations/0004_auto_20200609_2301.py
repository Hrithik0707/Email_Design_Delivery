# Generated by Django 2.2.6 on 2020-06-09 17:31

from django.db import migrations
import multiselectfield.db.fields
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_grps_gimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grps',
            name='contacts',
        ),
        migrations.AddField(
            model_name='grps',
            name='contacts',
            field=multiselectfield.db.fields.MultiSelectField(default=1, max_length=200, verbose_name=user.models.Contacts),
            preserve_default=False,
        ),
    ]