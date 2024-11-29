# Generated by Django 5.1.3 on 2024-11-29 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_portafolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/images/')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]