from django.test import TestCase
from myapp.models import MyModel

class MyModelTestCase(TestCase):
    
    def setUp(self):
        MyModel.objects.create(name="Test")

    def test_model_str(self):

        test_object = MyModel.objects.get(name="Test")
        self.assertEqual(test_object.__str__(), "Test")
