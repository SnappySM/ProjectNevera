from django.test import TestCase
from project_nevera_api.models import User

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

class UserTestCase(TestCase):
    def setUp(self):
        f = BytesIO()
        image = Image.new("RGB", (100,100))
        image.save(f, "png")
        f.seek(0)
        test_image = SimpleUploadedFile("test_image.png", f.read(), content_type="image/png")

        User.objects.create(mail="test@mail.com", username="TestUsername", bio="Test bio", avatar=test_image)

    def test_user_creation(self):
        user = User.objects.get(mail="test@mail.com")
        self.assertEqual(user.username, "TestUsername")
        self.assertEqual(user.bio, "Test bio")
        self.assertTrue(user.avatar.name.startswith("test_image"))