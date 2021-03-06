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
            field=models.CharField(blank=True, max_length=150, verbose_name='director'),  # noqa:501
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.CharField(blank=True, max_length=150, verbose_name='producer'),  # noqa:501
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='title'),  # noqa:501
        ),
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.CharField(blank=True, max_length=50, verbose_name='age'),  # noqa:501
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='gender'),  # noqa:501
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='name'),  # noqa:501
        ),
    ]
