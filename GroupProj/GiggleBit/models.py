from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

def get_path(instance,filename):
    return '/'.join([instance.uploader.username, 'images',filename])

def get_prof_pic_path(instance,filename):
    return '/'.join([instance.uploader.username, 'profile_images',filename])

class userprofile(models.Model): #additional user stuff
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    profile_pic = models.ImageField(upload_to=get_prof_pic_path)
    bio = models.CharField(max_length=512)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.user.username)
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
    uploader = models.ForeignKey(User)
    #uploader now must be defind in the form before the image and a user is
    #required to upload so we can have anemuse uploads
    #may cause random crashing if user is not defend eg if a pic if draged to upload
    #when not logged in will have to implement extra eroor cheacking
    picture = models.ImageField(upload_to = get_path)
    #also i want to point out this is very hacky and bad
    category = models.ManyToManyField(Category)
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
