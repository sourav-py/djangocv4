# Generated by Django 2.2.2 on 2019-06-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_auto_20190617_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='day19',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day20',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day21',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day22',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day23',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day24',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='day25',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
    ]
