# Generated by Django 3.2.13 on 2022-04-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20220420_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ispaid',
            field=models.BooleanField(default=False),
        ),
    ]
