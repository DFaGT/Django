# Generated by Django 4.2.1 on 2023-05-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20230525_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeCoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='adress',
            new_name='address',
        ),
        migrations.AddField(
            model_name='school',
            name='city',
            field=models.CharField(blank=True, choices=[('E', '西東京市'), ('J', '東久留米市'), ('H', '新座市'), ('O', '練馬区'), ('P', '小平市')], max_length=10),
        ),
        migrations.AlterField(
            model_name='parent',
            name='postal_code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='school',
            name='classification',
            field=models.CharField(choices=[('E', '小学校'), ('J', '中学校'), ('H', '高校'), ('O', 'その他')], max_length=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
