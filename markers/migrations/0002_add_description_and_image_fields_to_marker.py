# Generated by Django 3.2.8 on 2021-11-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='description',
            field=models.TextField(default='marker description'),
        ),
        migrations.AddField(
            model_name='marker',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]