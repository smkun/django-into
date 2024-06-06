from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual company ID

    def __str__(self):
        return self.name
