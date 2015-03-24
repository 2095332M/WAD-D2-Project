from django.test import TestCase
from GiggleBit.models import Category , Image ,User,Userprofile
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

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

class testViews(TestCase):

    def test_index_view_no_images(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no images present.")
        self.assertQuerysetEqual(response.context['images'], [])


def add_cat(name, views=0,):
    c = Category.objects.get_or_create(name=name, views=views)[0]
    return c


def add_user(username,password,bio="test",profile_pic= "test.jpg"):
    u = User.objects.create_user(username=username,password=password)
    up = Userprofile.objects.get_or_create(user=u, profile_pic=image_loc + profile_pic, bio=bio)[0]
    return up

def add_image(name,uploader,categories, filename,views =0):
    i = Image.objects.get_or_create(name=name,uploader=uploader,picture = image_loc + filename, views=views,upload_date = datetime.now() )[0]
    for category in categories:
        i.category.add(category)
    return i

def add_comment(user,image,com="test"):
    c = Comment.objects.get_or_create(user=user,image=image,comment=com)
    return c


def add_like(user,image):
    l = Liked.objects.get_or_create(user=user,image=image)
    return l

def add_fav_category(user,cat):
    fc = Fav_category.objects.get_or_create(user=user,category=cat)
    return fc
