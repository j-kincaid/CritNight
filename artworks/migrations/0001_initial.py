# Generated by Django 3.2.16 on 2023-01-13 23:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='')),
                ('dimensions', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]