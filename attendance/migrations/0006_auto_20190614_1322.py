# Generated by Django 2.2.2 on 2019-06-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_delete_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='friday',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='monday',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='saturday',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='thursday',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='tuesday',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='wednesday',
            field=models.CharField(choices=[('Present', 'P'), ('Absent', 'A'), ('NA', 'NA')], default='NA', max_length=10),
        ),
    ]
