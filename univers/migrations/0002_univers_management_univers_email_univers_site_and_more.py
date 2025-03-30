# Generated by Django 4.2.3 on 2024-02-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='univers',
            name='Management',
            field=models.CharField(default=1, max_length=200, verbose_name='Руководство'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='univers',
            name='email',
            field=models.CharField(default=1, max_length=200, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='univers',
            name='site',
            field=models.CharField(default=1, max_length=200, verbose_name='Сайт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='univers',
            name='start_date',
            field=models.CharField(default=2, max_length=200, verbose_name='Год основания'),
            preserve_default=False,
        ),
    ]
