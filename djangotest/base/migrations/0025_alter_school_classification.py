# Generated by Django 4.2.1 on 2023-06-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='classification',
            field=models.CharField(choices=[('小学校', '小学校'), ('中学校', '中学校'), ('高校', '高校'), ('その他', 'その他')], max_length=10),
        ),
    ]
