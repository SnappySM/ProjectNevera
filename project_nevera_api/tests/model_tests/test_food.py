from django.test import TestCase
from project_nevera_api.models import Food

class FoodTestCase(TestCase):
    def setUp(self):
        self.testFood = Food.objects.create(name="egg", quantity=6, quantity_unit="u")

    def test_food_creation(self):
        food = Food.objects.get(id=self.testFood.id)
        self.assertEqual(food.name, "egg")
        self.assertEqual(food.quantity, 6)
        self.assertEqual(food.quantity_unit, "u")