from django.db import models

# Create your models here.

class GenderChoices(models.TextChoices):
	Male = "男", "男"
	Female = "女", "女"
	Other = "その他", "その他"

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

class GradeCoices(models.TextChoices):
	Elementary1st = "小学1年性", "小学1年性"
	Elementary2nd = "小学2年性", "小学2年性"
	Elementary3rd = "小学3年性", "小学3年性"
	Elementary4th = "小学4年性", "小学4年性"
	Elementary5th = "小学5年性", "小学5年性"
	Elementary6th = "小学6年性", "小学6年性"
	JuniorHigh1st = "中学1年性", "中学1年性"
	JuniorHigh2nd = "中学2年性", "中学2年性"
	JuniorHigh3rd = "中学3年性", "中学3年性"
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
	exam_01 = models.DateField(auto_now=False, null=True)
	exam_02 = models.DateField(auto_now=False, null=True)
	exam_03 = models.DateField(auto_now=False, null=True)
	exam_04 = models.DateField(auto_now=False, null=True)
	exam_05 = models.DateField(auto_now=False, null=True)
	def __str__(self):
		return self.name

class Parent(models.Model):
	STATUS_TYPES = StatusChoices.choices
	parent_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	status = models.CharField(max_length=10, choices=STATUS_TYPES,blank=True)

	def __str__(self):
		return self.name

class Student(models.Model):
	GENDER_TYPES = GenderChoices.choices
	GRADE_TYPES = GradeCoices.choices
	STATUS_TYPES = StatusChoices.choices
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	name_kana = models.CharField(max_length=100, null=True)
	birthday = models.DateField(auto_now=False)
	gender = models.CharField(max_length=10, choices=GENDER_TYPES)
	sibling = models.BooleanField()
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
	grade = models.CharField(max_length=10, choices=GRADE_TYPES,blank=True)
	status = models.CharField(max_length=10, choices=STATUS_TYPES,blank=True)

	def __str__(self):
		return self.name

