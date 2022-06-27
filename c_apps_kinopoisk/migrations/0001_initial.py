# Generated by Django 4.0.1 on 2022-01-30 19:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='возраст')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(upload_to='media/c_apps_kinopoisk/actors/%Y/%m/%d/', verbose_name='изображение актера')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='категория')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='жанр')),
                ('description', models.TextField(verbose_name='описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('tagline', models.CharField(default='', max_length=150, verbose_name='слоган')),
                ('description', models.TextField(verbose_name='описание')),
                ('poster', models.ImageField(upload_to='media/c_apps_kinopoisk/posters/%Y/%m/%d/', verbose_name='poster')),
                ('year', models.PositiveSmallIntegerField(default=2022, verbose_name='дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='страна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='премьера в мире')),
                ('budget', models.PositiveIntegerField(default=0, verbose_name='бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, verbose_name='сборы в США')),
                ('fees_in_world', models.PositiveIntegerField(default=0, verbose_name='сборы в мире')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='c_apps_kinopoisk.Actor', verbose_name='актер')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='c_apps_kinopoisk.category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='c_apps_kinopoisk.Actor', verbose_name='режисер')),
                ('genres', models.ManyToManyField(to='c_apps_kinopoisk.Genre', verbose_name='жанр')),
            ],
        ),
        migrations.CreateModel(
            name='RattingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='значение')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=6000)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_apps_kinopoisk.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='c_apps_kinopoisk.reviews')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='ip адресс')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_apps_kinopoisk.movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_apps_kinopoisk.rattingstar')),
            ],
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовки')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(upload_to='media/c_apps_kinopoisk/posters/%Y/%m/%d/', verbose_name='изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_apps_kinopoisk.movie', verbose_name='фильм')),
            ],
        ),
    ]
