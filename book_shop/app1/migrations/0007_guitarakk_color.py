# Generated by Django 2.2.6 on 2019-10-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20191010_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitarakk',
            name='color',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
