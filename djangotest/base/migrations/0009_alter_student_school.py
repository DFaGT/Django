# Generated by Django 4.2.1 on 2023-05-18 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.school'),
        ),
    ]
