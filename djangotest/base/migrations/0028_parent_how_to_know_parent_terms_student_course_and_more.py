# Generated by Django 4.2.1 on 2023-06-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_school_exam_01_school_exam_02_school_exam_03_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='how_to_know',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='terms',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(blank=True, choices=[('個別指導(月2回)', '個別指導(月2回)'), ('個別指導(月4回)', '個別指導(月4回)'), ('個別指導(月8回)', '個別指導(月8回)'), ('通い放題ベーシック', '通い放題ベーシック'), ('通い放題ライト', '通い放題ライト'), ('通い放題ミニ', '通い放題ミニ'), ('小学生本科', '小学生本科'), ('小学生総合', '小学生総合'), ('ロボット教室', 'ロボット教室'), ('プログラミング教室', 'プログラミング教室')], max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='introducer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, choices=[('小学1年生', '小学1年生'), ('小学2年生', '小学2年生'), ('小学3年生', '小学3年生'), ('小学4年生', '小学4年生'), ('小学5年生', '小学5年生'), ('小学6年生', '小学6年生'), ('中学1年生', '中学1年生'), ('中学2年生', '中学2年生'), ('中学3年生', '中学3年生'), ('高校1年生', '高校1年生'), ('高校2年生', '高校2年生'), ('高校3年生', '高校3年生')], max_length=10),
        ),
    ]
