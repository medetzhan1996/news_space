# Generated by Django 4.2.3 on 2024-02-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Univers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='photos_news/')),
                ('content', models.TextField()),
                ('src', models.TextField()),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
