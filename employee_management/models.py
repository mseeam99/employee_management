from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    position = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Employee"  # Match the table name in MySQL


class Education(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Link to Employee
    collegename = models.CharField(max_length=100)
    address = models.TextField()
    degreecompleted = models.CharField(max_length=100)
    major = models.CharField(max_length=50)
    gpa = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.collegename} ({self.degreecompleted})"

    class Meta:
        db_table = "Education"  # Match the table name in MySQL


class Office(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Foreign Key to Employee
    officeName = models.CharField(max_length=100)
    address = models.TextField()
    year = models.IntegerField()
    totalEmployee = models.IntegerField()
    establishedYear = models.IntegerField()
    netWorth = models.FloatField()

    def __str__(self):
        return self.officeName

    class Meta:
        db_table = "Office"  # Match the table name in MySQL
