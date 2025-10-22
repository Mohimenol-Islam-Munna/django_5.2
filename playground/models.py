from django.db import models

class Address(models.Model):
    village = models.CharField(max_length=30)
    union = models.CharField(max_length=30)
    upazila = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=30)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    email = models.EmailField()
    class_name = models.ForeignKey('ClassName', on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)


class ClassName(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    teachers = models.ManyToManyField("Teacher")


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    established_year = models.IntegerField()

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    hire_date = models.DateField()
    