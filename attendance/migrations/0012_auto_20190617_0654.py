# Generated by Django 2.2.2 on 2019-06-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20190617_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='day10',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day11',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day12',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day13',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day14',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day15',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
    ]