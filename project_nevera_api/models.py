from django.db import models

# Create your models here.
class Refrigerator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.id

class User(models.Model):
    mail = models.EmailField(primary_key=True)
    username = models.CharField()
    bio = models.TextField()
    avatar = models.ImageField()
    refrigerator = models.ForeignKey(Refrigerator, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.mail

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
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_unit = models.CharField(choices=UNIT_TYPES)

    class Meta:
        unique_together = ("name", "quantity", "quantity_unit")

    def __str__(self):
        return self.name + " " + self.quantity + " " + self.quantity_unit

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    expirationDate = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    refrigerator = models.ForeignKey(Refrigerator, on_delete=models.CASCADE)

    def __str__(self):
        return self.id