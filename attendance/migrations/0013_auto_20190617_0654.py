# Generated by Django 2.2.2 on 2019-06-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_auto_20190617_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='day16',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day17',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day18',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
    ]
