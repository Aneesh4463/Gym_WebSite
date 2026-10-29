
from django.db import models

class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plan_name


class TrainingProgram(models.Model):
    program_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.program_name




class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='equipment/',
        blank=True,
        null=True
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    item_name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.item_name}"



class Supplement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='supplements/',
        blank=True,
        null=True
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class PersonalTrainingPackage(models.Model):
    package_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=50)
    sessions = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.package_name
