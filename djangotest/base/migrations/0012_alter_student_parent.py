# Generated by Django 4.2.1 on 2023-05-18 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_student_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.parent'),
        ),
    ]
