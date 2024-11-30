
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    position = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()

    class Meta:
        db_table = "Employee"
        indexes = [
            models.Index(fields=['position']),  # Index for filtering by position
            models.Index(fields=['sex']),  # Index for filtering by sex
        ]


class Education(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    collegename = models.CharField(max_length=100)
    address = models.TextField()
    degreecompleted = models.CharField(max_length=100)
    major = models.CharField(max_length=50)
    gpa = models.FloatField()
    year = models.IntegerField()

    class Meta:
        db_table = "Education"
        indexes = [
            models.Index(fields=['degreecompleted']),  # Index for filtering by degree
            models.Index(fields=['major']),  # Index for filtering by major
            models.Index(fields=['gpa']),  # Index for filtering by GPA
        ]


class Office(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    officeName = models.CharField(max_length=100)
    address = models.TextField()
    year = models.IntegerField()
    totalEmployee = models.IntegerField()
    establishedYear = models.IntegerField()
    netWorth = models.FloatField()

    class Meta:
        db_table = "Office"
        indexes = [
            models.Index(fields=['officeName']),  # Index for filtering by office name
            models.Index(fields=['establishedYear']),  # Index for ordering or filtering by established year
        ]


class PreviousEmployee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    position = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Previous Employee: {self.name} (ID: {self.employee_id})"

    class Meta:
        db_table = "PreviousEmployee"
