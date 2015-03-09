import os
from PIL import Image
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GroupProj.settings')

import django
django.setup()

from GiggleBit.models import *
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
image_loc = os.path.join(BASE_DIR,'/static/images/test.jpg')

def populate():

    names = "abcdefghij"

    cats =[]
    for x in range(10):
        cats += [add_cat(names[x])]

    users = []
    users += [add_user("a","a")]
    users += [add_user("b","b")]

    images =[]
    for user in users:
        for x in range(5):
            if user.username == "b":
                images += [add_image(names[x+5],user,cats[x+5])]
            else:
                images += [add_image(names[x],user,cats[x])]

    for x in range(len(images)):
            if x%3==0:
                add_like(users[0],images[x])
                add_comment(users[0],images[x])
            elif x%3 == 1:
                add_like(users[1],images[x])
                add_comment(users[1],images[x])
            else:
                add_like(users[0],images[x])
                add_like(users[1],images[x])
                add_comment(users[0],images[x])
                add_comment(users[1],images[x])

    for x in range(len(cats)):
        if x%2 ==0:
            add_fav_category(users[0],cats[x])
        else:
            add_fav_category(users[1],cats[x])


def add_cat(name, views=0,):
    c = Category.objects.get_or_create(name=name, views=views)[0]
    return c

def add_user(username,password,bio="test"):
    u = User.objects.create_user(username=username,password=password)
    up = userprofile.objects.get_or_create(user=u,bio=bio,profile_pic = image_loc)
    return u

def add_image(name,uploader,Cat,views=0):
    i = Image.objects.get_or_create(name=name,uploader=uploader,picture = image_loc, views=views,upload_date = datetime.now() )[0]
    i.Category.add(Cat)
    return i

def add_comment(user,image,com="test"):
    c = comment.objects.get_or_create(user=user,image=image,comment=com)
    return c


def add_like(user,image):
    l = liked.objects.get_or_create(user=user,image=image)
    return l

def add_fav_category(user,cat):
    fc = fav_category.objects.get_or_create(user=user,category=cat)
    return fc

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
    print "complete"
