# Generated by Django 2.2.2 on 2019-06-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20190617_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='day2',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=100),
        ),
    ]
