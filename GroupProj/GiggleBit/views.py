from django.shortcuts import render

from django.http import HttpResponse

from django.core.paginator import Paginator

from operator import attrgetter

from GiggleBit.models import *

from GiggleBit.forms import UserProfileForm

#CHAPTER 19 of rango book is basically essential for our app.

#super sick home page
def index(request):
    all_images = Image.objects.all()
    p= Paginator(all_images,16);
    try:
        content_dict = {'new_images': p.page(1)}
    except:
        content_dict = {}

    return render(request,'gigglebit/index.html', content_dict)

#similar/same as /category/ in rango
def tilde(request,tilde_slug):

    content_dict = {}
    category = Category.objects.get(slug=tilde_slug)
    try:
        content_dict['category_name'] = category.name
        all_images = Image.objects.filter(category=category)
        tilde_images = [all_images[:4],all_images[:4],all_images[:4],all_images[:4]]
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

def register_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                profile.user = user
                profile.picture = request.FILES['picture']
                profile.save()
        return index(request)
    else:
        form = UserProfileForm(request.GET)
        return render(request, 'gigglebit/profile_registration.html', {'profile_form': form})
