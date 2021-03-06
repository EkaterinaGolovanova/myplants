# Generated by Django 3.1.6 on 2021-02-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20210206_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='description',
        ),
        migrations.AddField(
            model_name='plant',
            name='botanical_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='hardiness_zones',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='mature_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='native_area',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='soil_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='sun_exposure',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='toxicity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
