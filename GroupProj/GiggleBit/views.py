from django.shortcuts import render
from django.http import HttpResponse

from GiggleBit.models import Image

#CHAPTER 19 of rango book is basically essential for our app.


#super sick home page
def index(request):

    new_images = Image.objects.all()
    content_dict = {'new_images': new_images}
    return render(request,'gigglebit/index.html', content_dict)

#similar/same as /category/ in rango
def tilde(request):
    return HttpResponse("IMPLEMENT ME")


#like add_page but needs to deal with multiple ~'s per image
#and is accesible from all other pages
def add_image(request):
    return HttpResponse("IMPLEMENT ME")


#image/unique_identifier/ one for each image, need random id creator
def image(request):
    return HttpResponse("IMPLEMENT ME")


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
    return HttpRespone("Produced by Stephen McMorran, Dillon Stevenson, Stuart Mackle and Kelvin Fowler")
