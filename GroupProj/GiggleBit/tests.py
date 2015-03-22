from django.test import TestCase
from GiggleBit.models import Category , Image ,User,Userprofile
from django.template.defaultfilters import slugify

#files
BASE_DIR = os.path.dirname(__file__)
image_loc = os.path.join(BASE_DIR,'/static/images/')

# Create your tests here.


def createImage():
    user = User(username="hi",password="x")
    user.save()
    up = Userprofile(user=user,bio="how are you")
    up.save()
    i = Image(name="test",uploader=up,picture = image_loc + "test.jpg", views=0,upload_date = datetime.now())
    i.save()
    return i
    
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
        self.assertEquals(cat.views,0)
        x = cat.views
        cat.views = x + 1
        self.assertEquals(cat.views,1)

class userTest(TestCase):

    def test_user_has_a_name(self):
        user = User(username="hi",password="x")
        user.save()
        self.assertEquals(user.username,"hi")

    def test_user_has_a_password(self):
         user = User(username="hi",password="x")
         user.save()
         self.assertEquals(user.password,"x")

    def test_userprofile_can_be_created(self):
        user = User(username="hi",password="x")
        user.save()
        up = Userprofile(user=user,bio="how are you")
        up.save()
        self.assertEquals(up.user,user)
        self.assertEquals(up.bio,"how are you")

class imageTest(TestCase):

    def test_image_has_name(self):
