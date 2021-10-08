from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    description = models.CharField(max_length=250, null=True)
    userRole = models.ForeignKey("Role", on_delete= models.PROTECT, related_name= "Roles", null = True)
    


class Role(models.Model):
    type = models.CharField(max_length=30, null = True)
    
    def __str__(self):
        return f"{self.type}"