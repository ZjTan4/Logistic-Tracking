from cProfile import label
from pyexpat import model
from unicodedata import category
from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    name = models.CharField(max_length=50, default="unknown")
    description = models.TextField(max_length=200, default="")

    label = models.CharField(max_length=50, default="uncategorized")
