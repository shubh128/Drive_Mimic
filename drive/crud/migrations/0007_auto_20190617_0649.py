# Generated by Django 2.2.2 on 2019-06-17 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_auto_20190617_0647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='uploader',
            new_name='user',
        ),
    ]