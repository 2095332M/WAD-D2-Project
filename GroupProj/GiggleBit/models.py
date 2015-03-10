from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class userprofile(models.Model): #additional user stuff
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    profile_pic = models.ImageField(upload_to='profile_images')
    bio = models.CharField(max_length=512)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.user.name)
        super(userprofile, self).save(*args, **kwargs)

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
    picture = models.ImageField(upload_to="images")
    uploader = models.ForeignKey(User)
    Category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    upload_date = models.DateTimeField()

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class comment(models.Model):
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)
    comment = models.CharField(max_length=512)

    def __unicode__(self):
        return self.comment


class liked(models.Model):
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)

class fav_category(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
