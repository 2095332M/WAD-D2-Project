from django.test import TestCase
from GiggleBit.models import Category
from django.template.defaultfilters import slugify
# Create your tests here.

class CatagoryTest(TestCase):

    def test_cat_has_a_slug(self):
        cat = Category(name="linux")
        cat.save()
        self.assertEquals(cat.slug,slugify("linux"))

    def test_cat_has_a_name(self):
        cat = Category(name="linux")
        cat.save()
        self.assertEquals(cat.name,"linux")

    def test_cat_has_views(self):
        cat = Category(name="linux")
        cat.save()
        self.assertEquals(cat.views,-1)
