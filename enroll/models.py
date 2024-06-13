from django.db import models

# Create your models here.

class Student(models.Model):
    std_id=models.IntegerField()
    std_name=models.CharField(max_length=40)
    std_email=models.EmailField(max_length=40)
    std_pass=models.CharField(max_length=40)

    def __str__(self):
        return self.std_name