from django.db import models

# Create your models here.

GENDER_CHOICES = [
	('M', '男'),
	('F', '女'),
	('O', 'その他'),
]

CLASS_CHOICES = [
	('E', '小学校'),
	('J', '中学校'),
	('H', '高校'),
	('O', 'その他'),
]

CITY_CHOICES = [
	('E', '西東京市'),
	('J', '東久留米市'),
	('H', '新座市'),
	('O', '練馬区'),
	('P', '小平市'),
]

class GradeCoices(models.Model):
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
	school_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	classification = models.CharField(max_length=10, choices=CLASS_CHOICES)
	city = models.CharField(max_length=10, choices=CITY_CHOICES,blank=True)
 
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
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	birthday = models.DateField(auto_now=False)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	sibling = models.BooleanField()
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
 
	def __str__(self):
		return self.name

