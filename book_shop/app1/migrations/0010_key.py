# Generated by Django 2.2.6 on 2019-10-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_equipments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
            ],
        ),
    ]
