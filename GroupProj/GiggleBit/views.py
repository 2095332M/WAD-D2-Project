from django.shortcuts import render, render_to_response
from django.shortcuts import redirect

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage

from operator import attrgetter

from GiggleBit.models import *

from GiggleBit.forms import *

from django.template import RequestContext

import datetime

#CHAPTER 19 of rango book is basically essential for our app.

#super sick home page
def index(request,page=1):
    #Removes the last "/" and then find the last / in the url then removes everything past that, i.e /tilde/2344/ becomes /tilde/
    href_clean = request.get_full_path()[:request.get_full_path()[:-1].rfind("/") + 1]
    content_dict = {}
    all_images = Image.objects.all()
    p= Paginator(all_images,16, allow_empty_first_page=False);
    
    try:
        content_dict['new_images'] = p.page(page)
        if(p.page(page).has_next()):
            content_dict['next_page'] = href_clean + str(int(page) + 1)
    except EmptyPage:
        if page == "1":
            content_dict['error_message'] = 'There are no images to display, sorry!'
        else:
            return redirect('/gigglebit/' + str(p.num_pages) + '/')


    content_dict['page_header'] = 'Popular on gigglebit today'
    if page > "1":
        content_dict['last_page'] = href_clean + str(int(page) - 1)
    return render(request,'gigglebit/imagedisplay.html', content_dict)

#similar/same as /category/ in rango
def tilde(request,tilde_slug,page=1):
    #Removes the last "/" and then find the last / in the url then removes everything past that, i.e /tilde/2344/ becomes /tilde/
    href_clean = request.get_full_path()[:request.get_full_path()[:-1].rfind("/") + 1]
    content_dict = {}
    category = Category.objects.get(slug=tilde_slug)
    all_images = Image.objects.filter(category=category)
    p = Paginator(all_images,16,allow_empty_first_page=False)
    
    try:
        content_dict['page_header'] = category.name
    except Category.DoesNotExist:
        content_dict['page_header'] = "This Category doesn't exist"
        return render(request,'gigglebit/imagedisplay.html', content_dict)
    try:
        content_dict['new_images'] = p.page(page)
        if(p.page(page).has_next()):
            content_dict['next_page'] = href_clean + str(int(page) + 1)
    except EmptyPage:
        if page == "1":
            content_dict['error_message'] = 'There are no images to display, sorry!'
        else:
            return redirect(href_clean + str(p.num_pages))
    return render(request,'gigglebit/imagedisplay.html', content_dict)


#like add_page but needs to deal with multiple ~'s per image
#and is accesible from all other pages
def add_image(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            newimage = image_form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            
            newimage.uploader = user
            newimage.picture = request.FILES['picture']
            newimage.upload_date = datetime.datetime.now()
            newimage.save()
            

        return index(request)
    else:
        image_form = ImageForm()

    content_dict = {'image_form': image_form}
    return render(request, 'GiggleBit/addimage.html', content_dict)


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
