from django.test import TestCase
from .models import Category, Subcategory, Activity

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Work')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Work')

    def test_category_update(self):
        self.category.name = 'Personal'
        self.category.save()
        self.assertEqual(Category.objects.get(id=self.category.id).name, 'Personal')

    def test_category_delete(self):
        category_id = self.category.id
        self.category.delete()
        self.assertFalse(Category.objects.filter(id=category_id).exists())

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Work')

class SubcategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Work')
        cls.subcategory = Subcategory.objects.create(name='Meetings', category=cls.category)

    def test_subcategory_creation(self):
        self.assertEqual(self.subcategory.name, 'Meetings')
        self.assertEqual(self.subcategory.category.name, 'Work')

    def test_subcategory_update(self):
        self.subcategory.name = 'Conference'
        self.subcategory.save()
        self.assertEqual(Subcategory.objects.get(id=self.subcategory.id).name, 'Conference')

    def test_subcategory_delete(self):
        subcategory_id = self.subcategory.id
        self.subcategory.delete()
        self.assertFalse(Subcategory.objects.filter(id=subcategory_id).exists())

    def test_subcategory_str(self):
        self.assertEqual(str(self.subcategory), 'Work - Meetings')

    def test_delete_category_cascade(self):
        self.category.delete()
        self.assertFalse(Subcategory.objects.filter(id=self.subcategory.id).exists())

class ActivityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Work')
        cls.subcategory = Subcategory.objects.create(name='Meetings', category=cls.category)
        cls.activity = Activity.objects.create(name='Team Meeting', subcategory=cls.subcategory)

    def test_activity_creation(self):
        self.assertEqual(self.activity.name, 'Team Meeting')
        self.assertEqual(self.activity.subcategory.name, 'Meetings')

    def test_activity_update(self):
        self.activity.name = 'Client Meeting'
        self.activity.save()
        self.assertEqual(Activity.objects.get(id=self.activity.id).name, 'Client Meeting')

    def test_activity_delete(self):
        activity_id = self.activity.id
        self.activity.delete()
        self.assertFalse(Activity.objects.filter(id=activity_id).exists())

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'Meetings - Team Meeting')

    def test_delete_subcategory_cascade(self):
        self.subcategory.delete()
        self.assertFalse(Activity.objects.filter(id=self.activity.id).exists())
