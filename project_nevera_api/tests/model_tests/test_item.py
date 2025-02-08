from django.test import TestCase
from project_nevera_api.models import Item
from project_nevera_api.models import Food
from project_nevera_api.models import Refrigerator


class ItemTestCase(TestCase):
    def setUp(self):
        refrigerator = Refrigerator.objects.create(name="TestRefrigerator", description="This is a test refrigerator")
        food = Food.objects.create(name="egg", quantity=6, quantity_unit="u")
        Item.objects.create(price=2.50, food=food, refrigerator=refrigerator)

    def test_item_creation(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.price, 2.50)
        self.assertEqual(item.food.name, "egg")
        self.assertEqual(item.refrigerator.name, "TestRefrigerator")