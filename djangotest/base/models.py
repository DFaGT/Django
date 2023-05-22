from django.db import models

# Create your models here.

class dbtest(models.Model):
	text = models.CharField(max_length=100)
	number = models.IntegerField()
	
	def __str__(self):
		return self.text

class School(models.Model):
	school_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	classification = models.CharField(max_length=100)
 
	def __str__(self):
		return self.name

class Parent(models.Model):
	parent_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	postal_code = models.PositiveIntegerField()
	adress = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	birthday = models.DateField(auto_now=False)
	gender = models.CharField(max_length=10)
	sibling = models.BooleanField()
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
 
	def __str__(self):
		return self.name

