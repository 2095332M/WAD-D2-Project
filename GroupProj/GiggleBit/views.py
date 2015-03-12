from django.shortcuts import render
from django.http import HttpResponse

from operator import attrgetter

from GiggleBit.models import *

#CHAPTER 19 of rango book is basically essential for our app.

#super sick home page
def index(request,filter='new'):
    all_images = Image.objects.all()
    al_images_sorted_new = sorted(all_images,key=attrgetter('upload_date'),reverse=True)
    #Testing one
    new_images = [all_images[:4],all_images[:4],all_images[:4],all_images[:4]]
    #Proper one, commenting out for testing
    #Creates a list of QueryList's of size 4 (grid width)
    #Currently parses 16 images (4 loops of list comprehension)
    #new_images = [ [all_images[i],all_images[i+1],all_images[i+2],all_images[i+3]] for i in xrange(4)]

    content_dict = {'new_images': new_images}
    return render(request,'gigglebit/index.html', content_dict)

#similar/same as /category/ in rango
def tilde(request,tilde_slug):

    content_dict = {}
    category = Category.objects.get(slug=tilde_slug)
    try:
        content_dict['category_name'] = category.name
        tilde_images = Image.objects.filter(category=category)
        content_dict['tilde_images'] = tilde_images
        content_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request,'gigglebit/tilde.html', content_dict)


#like add_page but needs to deal with multiple ~'s per image
#and is accesible from all other pages
def add_image(request):
    return HttpResponse("IMPLEMENT ME")


#image/unique_identifier/ one for each image, need random id creator
def image(request,image_slug):
    content_dict = {}
    image = Image.objects.get(slug=image_slug)
    content_dict['tildes'] = image.category.all()
    content_dict["image"] = image
    content_dict["comments"] = comment.objects.filter(image=image)
    content_dict["likes"] = len(liked.objects.filter(image=image))
    return render(request,"gigglebit/image.html",content_dict)


#REDIRECT PAGE for each image to track page views for sorting/displaying algorithms
#could be too hard within time frame to do algorithms but this view itself is ok
#basically exactly the same to rango's track_url
def track_url(request):
    return HttpResponse("IMPLEMENT ME")


#Probabaly is necessary to return results of searching images
def search(request):
    return HttpResponse("IMPLEMENT ME")

#About Page
def about(request):
    return render(request, 'gigglebit/about.html')
