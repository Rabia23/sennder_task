# Generated by Django 3.2.1 on 2021-06-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=150, verbose_name='director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.CharField(blank=True, max_length=150, verbose_name='producer'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.CharField(blank=True, max_length=50, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='name'),
        ),
    ]
