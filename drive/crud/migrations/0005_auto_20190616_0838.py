# Generated by Django 2.2.2 on 2019-06-16 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20190616_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
