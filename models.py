from django.db import models


class ContactInfo(models.Model):
    mobileNumber = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=15)
    emailID = models.EmailField(max_length=50)


class Person(ContactInfo):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
