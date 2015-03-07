import os
from PIL import Image
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from GiggleBit.models import *

image = Image.open("static/images/test.jpg")

def populate():


    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_cat(cat, views=0,):
    c = Catagory.objects.get_or_create(category=cat, views=views)[0]
    return p

def add_image(name,uploader,catagory,views=0,image):
    i = image.objects.get_or_create(name=name,views=views)[0]
    return i

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
