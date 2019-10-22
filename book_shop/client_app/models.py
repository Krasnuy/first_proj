from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    TYPE_USER_VIEW = (
        ('fio', 'ФИО'),
        ('pseudo_name', 'Псевдоним'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=5000,
                           verbose_name=('Bio'),
                           blank=True, null=True)
    type_view = models.CharField(max_length=255,
                                 verbose_name=('Тип представления'),
                                 choices=TYPE_USER_VIEW,
                                 blank=True, null=True)
    pseudoname = models.CharField(max_length=255,
                                  verbose_name=('Псевдоним'),
                                  blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Comment(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField(max_length=1000, verbose_name='Текст комментария')


class Article(models.Model):
    PUSBLISH_STATUS = (
        ('publish', 'Да'),
        ('unpublish', 'Нет'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,
                             verbose_name='Title', blank=True,
                             null=True, default='')
    content = models.TextField()
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    status = models.CharField(max_length=55, verbose_name='Publish?', choices=PUSBLISH_STATUS)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return '{} {} '.format(self.title, self.create_at)

    def __repr__(self):
        return 'this is object in sqlite data base with unique id {}'.format(self.id)


class Demo(models.Model):
    name = models.CharField(max_length=255)
    int_examples = models.IntegerField(blank=True, null=True, default=0)
    float_examples = models.FloatField(blank=True, null=True, default=0.0)
    txt_examples = models.TextField(blank=True, null=True, default='')
    date_examples = models.DateField(blank=True, null=True, default='1995-05-12')
    date_time_examples = models.DateTimeField(auto_now_add=True,
                                              blank=True, null=True)
    bool_examples = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return '{}'.format(self.name)
