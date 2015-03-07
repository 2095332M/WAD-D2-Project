from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class userprofile(models.models): #additional user stuff
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=512)

    def __unicode__(self):
        return self.user.username

class image(models.models):
    name = models.CharField(max_length=128, unique=True)
    Image = models.ImageField(upload_to="images", blank=True)
    uploader = models.ForeignKey(user)
    Category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class comment(models.models):
    user = models.ForeignKey(user)
    image = models.ForeignKey(image)
    comment = models.CharField(max_lenght=512)

    def __unicode__(self):
        return self.comment

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class liked(models.Model):
    user = models.ForeignKey(user)
    image = models.ForeignKey(image)
