# Generated by Django 4.2.1 on 2023-05-25 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20230518_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', '男'), ('F', '女')], max_length=10),
        ),
    ]
