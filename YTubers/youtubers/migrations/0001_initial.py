# Generated by Django 3.2.25 on 2024-04-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('age', models.IntegerField()),
                ('video_url', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='media/youtuber/%Y/%m/')),
                ('height', models.IntegerField()),
                ('crew', models.CharField(max_length=255)),
                ('camera_type', models.CharField(max_length=255)),
                ('subs_count', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]