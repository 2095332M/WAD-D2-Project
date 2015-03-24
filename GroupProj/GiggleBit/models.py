from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

def get_path(instance,filename):
    return '/'.join([instance.uploader.user.username, 'images',filename])

def get_prof_pic_path(instance,filename):
    return '/'.join([instance.uploader.user.username, 'profile_images',filename])

class Userprofile(models.Model): #additional user stuff
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    profile_pic = models.ImageField(upload_to=get_prof_pic_path, default='test.jpg')
    bio = models.CharField(max_length=512)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Userprofile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Image(models.Model):

    name = models.CharField(max_length=128, unique=True)
    uploader = models.ForeignKey(Userprofile)
    likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to = get_path)
    category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    upload_date = models.DateTimeField()

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(Userprofile)
    image = models.ForeignKey(Image)
    comment = models.CharField(max_length=512)

    def __unicode__(self):
        return self.comment


class Liked(models.Model):
    user = models.ForeignKey(Userprofile)
    image = models.ForeignKey(Image)

class Fav_category(models.Model):
    user = models.ForeignKey(Userprofile)
    category = models.ForeignKey(Category)
