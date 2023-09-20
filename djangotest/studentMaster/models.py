from django.db import models
from django import forms
# Create your models here.

class GenderChoices(models.TextChoices):
	Male = "男", "男"
	Female = "女", "女"
	Other = "その他", "その他"

class HowToKnowChoices(models.TextChoices):
	Ans1 = "webサイト", "webサイト"
	Ans2 = "チラシ", "チラシ"
	Ans3 = "紹介", "紹介"
	Ans4 = "兄弟が通塾している", "兄弟が通塾している"
	Ans5 = "知人からの紹介", "知人からの紹介"
	Ans6 = "看板を見た", "看板を見た"
	Ans7 = "その他", "その他"

class ClassChoices(models.TextChoices):
	Elementary = "小学校", "小学校"
	JuniorHigh = "中学校", "中学校"
	High = "高校", "高校"
	Other = "その他", "その他"

class CityChoices(models.TextChoices):
	WestTokyo = "西東京市", "西東京市"
	HigashiKurume = "東久留米市", "東久留米市"
	Niiza = "新座市", "新座市"
	Nerima = "練馬区", "練馬区"
	Kodaira = "小平市", "小平市"

class StatusChoices(models.TextChoices):
	Atend = "通塾", "通塾"
	Closed = "休塾", "休塾"
	Retired = "退塾", "退塾"
	Trial = "体験", "体験"

class SubjectChoices(models.TextChoices):
	Math = "数学", "数学"
	English = "英語", "英語"
	Science = "理科", "理科"
	Social = "社会", "社会"
	Japanese = "国語", "国語"
	Other = "その他", "その他"

class CourseChoices(models.TextChoices):
	kobetu2 = "個別指導(月2回)", "個別指導(月2回)"
	kobetu4 = "個別指導(月4回)", "個別指導(月4回)"
	kobetu8 = "個別指導(月8回)", "個別指導(月8回)"
	basic = "通い放題ベーシック", "通い放題ベーシック"
	light = "通い放題ライト", "通い放題ライト"
	mini = "通い放題ミニ", "通い放題ミニ"
	honka = "小学生本科", "小学生本科"
	sogo = "小学生総合", "小学生総合"
	robot = "ロボット教室", "ロボット教室"
	programming = "プログラミング教室", "プログラミング教室"

class GradeCoices(models.TextChoices):
	Elementary1st = "小学1年生", "小学1年生"
	Elementary2nd = "小学2年生", "小学2年生"
	Elementary3rd = "小学3年生", "小学3年生"
	Elementary4th = "小学4年生", "小学4年生"
	Elementary5th = "小学5年生", "小学5年生"
	Elementary6th = "小学6年生", "小学6年生"
	JuniorHigh1st = "中学1年生", "中学1年生"
	JuniorHigh2nd = "中学2年生", "中学2年生"
	JuniorHigh3rd = "中学3年生", "中学3年生"
	High1st = "高校1年生", "高校1年生"
	High2nd = "高校2年生", "高校2年生"
	High3rd = "高校3年生", "高校3年生"

class dbtest(models.Model):
	text = models.CharField(max_length=100)
	number = models.IntegerField()
	
	def __str__(self):
		return self.text

class School(models.Model):
	SCHOOL_TYPES = CityChoices.choices
	CLASS_TYPES = ClassChoices.choices
	school_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	classification = models.CharField(max_length=10, choices=CLASS_TYPES)
	city = models.CharField(max_length=10, choices=SCHOOL_TYPES,blank=True)
	exam_01 = models.DateField(auto_now=False, blank=True, null=True)
	exam_02 = models.DateField(auto_now=False, blank=True, null=True)
	exam_03 = models.DateField(auto_now=False, blank=True, null=True)
	exam_04 = models.DateField(auto_now=False, blank=True, null=True)
	exam_05 = models.DateField(auto_now=False, blank=True, null=True)
	def __str__(self):
		return self.name

class Parent(models.Model):
	STATUS_TYPES = StatusChoices.choices
	HOWTOKNOW_TYPES = HowToKnowChoices.choices
	parent_id = models.AutoField(primary_key=True)
	last_name = models.CharField(max_length=100, null=True)
	first_name = models.CharField(max_length=100, null=True)
	postal_code = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	status = models.CharField(max_length=10, choices=STATUS_TYPES,blank=True)
	terms = models.BooleanField(null=True)
	how_to_know = models.CharField(max_length=100,choices=HOWTOKNOW_TYPES, null=True, blank=True)

	def __str__(self):
		full_name = f'{self.last_name} {self.first_name}' if self.first_name and self.last_name else ''
		return full_name or self.first_name or self.last_name or ''


class Student(models.Model):
	GENDER_TYPES = GenderChoices.choices
	GRADE_TYPES = GradeCoices.choices
	STATUS_TYPES = StatusChoices.choices
	COURSE_TYPES = CourseChoices.choices
	student_id = models.AutoField(primary_key=True)
	last_name = models.CharField(max_length=100, null=True)
	last_name_kana = models.CharField(max_length=100, null=True)
	first_name = models.CharField(max_length=100, null=True)
	first_name_kana = models.CharField(max_length=100, null=True)
	birthday = models.DateField(auto_now=False)
	gender = models.CharField(max_length=10, choices=GENDER_TYPES)
	sibling = models.BooleanField()
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE,blank=True, null=True)
	grade = models.CharField(max_length=10, choices=GRADE_TYPES,blank=True)
	status = models.CharField(max_length=10, choices=STATUS_TYPES,blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	introducer = models.CharField(max_length=100, null=True, blank=True)
	course = models.CharField(max_length=100, choices=COURSE_TYPES,blank=True)

	def __str__(self):
		return self.first_name if self.first_name and self.last_name else ''

