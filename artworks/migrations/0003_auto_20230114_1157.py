# Generated by Django 3.2.16 on 2023-01-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_auto_20230113_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='might_work',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='needs_work',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='what_works',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
