from django.db import models

# Create your models here.

class GenderChoices(models.TextChoices):
	Male = "M", "男"
	Female = "F", "女"
	Other = "O", "その他"

class ClassChoices(models.TextChoices):
	Elementary = "小学校", "小学校"
	JuniorHigh = "中学校", "中学校"
	High = "高校", "高校"
	Other = "その他", "その他"

class CityChoices(models.TextChoices):
	WestTokyo = "E", "西東京市"
	HigashiKurume = "J", "東久留米市"
	Niiza = "H", "新座市"
	Nerima = "O", "練馬区"
	Kodaira = "P", "小平市"

class StatusChoices(models.TextChoices):
	Atend = "A", "通塾"
	Closed = "C", "休塾"
	Retired = "R", "退塾"
	Trial = "T", "体験"

class GradeCoices(models.TextChoices):
	Elementary1st = "e1", "小学1年性"
	Elementary2nd = "e2", "小学2年性"
	Elementary3rd = "e3", "小学3年性"
	Elementary4th = "e4", "小学4年性"
	Elementary5th = "e5", "小学5年性"
	Elementary6th = "e6", "小学6年性"
	JuniorHigh1st = "j1", "中学1年性"
	JuniorHigh2nd = "j2", "中学2年性"
	JuniorHigh3rd = "j3", "中学3年性"
	High1st = "h1", "高校1年生"
	High2nd = "h2", "高校2年生"
	High3rd = "h3", "高校3年生"

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
 
	def __str__(self):
		return self.name

class Parent(models.Model):
	parent_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Student(models.Model):
	GENDER_TYPES = GenderChoices.choices
	GRADE_TYPES = GradeCoices.choices
	STATUS_TYPES = StatusChoices.choices
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	birthday = models.DateField(auto_now=False)
	gender = models.CharField(max_length=10, choices=GENDER_TYPES)
	sibling = models.BooleanField()
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
	grade = models.CharField(max_length=10, choices=GRADE_TYPES,blank=True)
	status = models.CharField(max_length=10, choices=STATUS_TYPES,blank=True)

	def __str__(self):
		return self.name

