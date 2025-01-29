from django.db import models

# Create your models here.
class User(models.Model):
    mail = models.EmailField(primary_key=True)
    username = models.CharField()
    bio = models.TextField()
    avatar = models.ImageField()

class Refrigerator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField(blank=True)

class Food(models.Model):
    UNIT_TYPES = {
        "u": "Units",
        "g": "Grams",
        "mg": "Milligrams",
        "kg": "Killograms",
        "l": "Liter",
        "cl": "Centiliter",
        "ml": "Milliliter"
    }
    name = models.CharField(primary_key=True)
    quantity = models.DecimalField(decimal_places=2)
    quantity_unit = models.CharField(choices=UNIT_TYPES)

class Item(models.Model):
    expirationDate = models.DateField(blank=True)
    price = models.DecimalField(decimal_places=2)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    refrigerator = models.ForeignKey(Refrigerator, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("food", "refrigerator")