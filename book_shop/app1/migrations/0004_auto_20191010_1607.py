# Generated by Django 2.2.6 on 2019-10-10 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20191010_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guitarakk',
            old_name='name',
            new_name='title',
        ),
    ]
