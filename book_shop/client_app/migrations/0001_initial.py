# Generated by Django 2.2.6 on 2019-10-21 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('int_examples', models.IntegerField(blank=True, default=0, null=True)),
                ('float_examples', models.FloatField(blank=True, default=0.0, null=True)),
                ('txt_examples', models.TextField(blank=True, default='', null=True)),
                ('date_examples', models.DateField(blank=True, default='1995-05-12', null=True)),
                ('date_time_examples', models.DateTimeField(auto_now_add=True, null=True)),
                ('bool_examples', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(max_length=1000, verbose_name='Текст комментария')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Bio')),
                ('type_view', models.CharField(blank=True, choices=[('fio', 'ФИО'), ('pseudo_name', 'Псевдоним')], max_length=255, null=True, verbose_name='Тип представления')),
                ('pseudoname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Псевдоним')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Title')),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('publish', 'Да'), ('unpublish', 'Нет')], max_length=55, verbose_name='Publish?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_app.Author')),
                ('comments', models.ManyToManyField(to='client_app.Comment')),
            ],
        ),
    ]
