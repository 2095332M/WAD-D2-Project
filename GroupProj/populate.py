import os
from PIL import Image
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GroupProj.settings')

import django
django.setup()

from GiggleBit.models import *
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
image_loc = os.path.join(BASE_DIR,'/static/images/')

def populate():

    names = "abcdefghij"
    
    #Users
    Dylan = add_user("Dylan","123", "Linux is love, linux is life","dylan.jpg")
    Kelvin = add_user("Kelvin","456", "WHY IS IT NOT WORKING?","kelvin.jpg")
    Stuart = add_user("Stuart","abc", "You're a douche if you make your own bio", "stuart.jpg")
    Stephen = add_user("Stephen","def","I'm a ghost!", "test.jpg")
    Test1 = add_user("Test","test","Test user", "test.jpg")
    Test2 = add_user("test","test","Test user", "test.jpg")
    
    #Categories
    linux = add_cat("linux", 10)
    mac = add_cat("mac", 5)
    windows = add_cat("windows", 6)
    maccirclejerk = add_cat("maccirclejerk",0)
    wad = add_cat("wad",2)
    
    #Images
    macbroken = add_image("When a mac breaks",Dylan,[maccirclejerk],"macbroken.jpg")
    macforchildren = add_image("Mac is for children, lol.", Dylan,[maccirclejerk],"macforchildren.jpg")
    macbin = add_image("What a mac pro should be used for", Stephen,[maccirclejerk], "macbin.jpg")
    
    linuxsudo = add_image("I love sudo", Stuart,[linux], "linuxsudo.jpg")
    linuxbuild = add_image("Mac is so much better for this very reason", Kelvin,[linux,mac],"linuxbuild.jpg")
    
    bugs = add_image("When you're developing your WAD project", Stuart, [wad],"bugs.jpg")
    compiledcode = add_image("That feeling", Kelvin,[wad], "compiledcode.jpg")
    hiddensemicolon = add_image("I've spent too much time trying to find the champ", Dylan,[wad],"hiddensemicolon.jpg")
	
	
    maclinuxwindows = add_image("1000 pounds wasted", Dylan, [windows,linux,mac,maccirclejerk],"maclinuxwindows.jpg")
    windowslinuxmac = add_image("Hate us", Stephen,[windows,linux,mac,maccirclejerk],"windowslinuxmac.jpg")
    
    
    #Likes
    
    add_like(Dylan,macbroken)
    add_like(Dylan,macbin)
    add_like(Dylan,windowslinuxmac)
    
    add_like(Stuart, bugs)
    add_like(Stuart, compiledcode)
    add_like(Stuart, linuxbuild)
    
    add_like(Kelvin,linuxsudo)
    add_like(Kelvin,windowslinuxmac)
    add_like(Kelvin,macforchildren)
    
    add_like(Stephen,hiddensemicolon)
    add_like(Stephen,bugs)
    add_like(Stephen,macbroken)
    
    #Comments
    
    add_comment(Stuart,bugs,"I'm hilarious")
    add_comment(Kelvin,bugs,"Get over yourself")
    add_comment(Kelvin,bugs,"The uppercase is accurate")
    
    add_comment(Dylan,macbin,"Haha, it isn't even a good bin!")
    add_comment(Stuart,macbin, "I'd totally buy it")
    add_comment(Stephen,macbin, "Mac user found!")
    
    add_comment(Kelvin,windowslinuxmac,"Atleast windows is getting slated")

    add_comment(Dylan, macbroken, "Like for like, follow for follow!")

    add_comment(Dylan, maclinuxwindows, "Like my first post plz")

    add_comment(Stuart,hiddensemicolon, "This is why python is the best")

    add_comment(Kelvin,compiledcode, "What's compiled code?")

    add_comment(Stephen, linuxsudo, "Sudo makes me break ubuntu, I hate it!")

    add_comment(Stuart, linuxbuild, "Mac works straight out the box")

    add_comment(Kelvin, macforchildren, "Wrong!")

    #Favourites
    add_fav_category(Dylan, linux)
    add_fav_category(Kelvin, wad)
    add_fav_category(Stuart, mac)
    add_fav_category(Stephen,windows)

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

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
    print "complete"
