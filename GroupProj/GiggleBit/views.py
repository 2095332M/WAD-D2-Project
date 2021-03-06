from django.shortcuts import render, render_to_response
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage

from operator import attrgetter

from GiggleBit.models import *

from GiggleBit.forms import *

from django.template import RequestContext

from datetime import datetime, timedelta

#-*- coding: utf-8 -*-

#CHAPTER 19 of rango book is basically essential for our app.

#super sick home page
def index(request,page=1):
    #Removes the last "/" and then find the last / in the url then removes everything past that, i.e /tilde/2344/ becomes /tilde/
    #removes ajax search string
    stripped_href = request.get_full_path()[:request.get_full_path().rfind('?')]



    #Of the form /gigglebit/<hot,top,new>/
    if stripped_href.count('/') > 4:
        href_clean = stripped_href[:stripped_href[:-1].rfind("/") + 1]
        image_filter = href_clean[-4:-1]
        href_clean = href_clean[:-4]
    else:
        image_filter = 'hot'
        href_clean = '/gigglebit/'
    content_dict = {}

    #Top/hot/new hyperlinks
    content_dict['hot_hyperlink'] = href_clean + 'hot/1/'
    content_dict['new_hyperlink'] = href_clean + 'new/1/'
    content_dict['top_hyperlink'] = href_clean + 'top/1/'

    #New images
    if image_filter == "new":
        filtered_images = Image.objects.order_by('-upload_date')
        content_dict['page_header'] = 'New images uploaded to GiggleBit'

    #Top images
    elif image_filter == "top":
        filtered_images = Image.objects.order_by('-likes')
        content_dict['page_header'] = 'Top images on all of GiggleBit'
    #Hot images
    else:
        current_datetime = datetime.now()
        #Gets the images in the last 12 hours and orders them by descending order
        twelve_hours_ago = current_datetime - timedelta(hours = 12)
        filtered_images = Image.objects.filter(upload_date__gte=twelve_hours_ago).order_by('-likes')
        content_dict['page_header'] = 'Popular on GiggleBit right now!'

    p = Paginator(filtered_images,16, allow_empty_first_page=False);
    try:
        content_dict['new_images'] = p.page(page)
	# check if not mod 4
        if((not (p.page(page).end_index() + 1 ) /4 == 0)):
			content_dict['not_mod4'] = 'True'
        if(p.page(page).has_next()):
            content_dict['next_page'] = href_clean + str(int(page) + 1)
            content_dict['display_page_links'] = True
    except EmptyPage:
        if page == "1":
            content_dict['error_message'] = 'There are no images to display, sorry!'
        else:
            return redirect('/gigglebit/' + str(p.num_pages) + '/')


    if page > "1":
        content_dict['last_page'] = href_clean + str(int(page) - 1)
        content_dict['display_page_links'] = True
    return render(request,'GiggleBit/imagedisplay.html', content_dict)

#similar/same as /category/ in rango
def tilde(request,tilde_slug,page=1):
    #Removes the last "/" and then find the last / in the url then removes everything past that, i.e /tilde/2344/ becomes /
    #Removes ajax search strings
    stripped_href = request.get_full_path()[:request.get_full_path().rfind('?')]
    if(stripped_href.count('/') > 4):
        #/gigglebit/tilde/<tildename>/<top,new,hot>/<pageno>/ becomes /tilde/<tn>/<t,h,n>/
        href_clean = request.get_full_path()[:request.get_full_path()[:-1].rfind("/") + 1]
        image_filter = href_clean[-4:-1]
        href_clean = href_clean[:-4]
    else:
        #/gigglebit/tilde/<tn>/
        href_clean = href_clean = request.get_full_path()
        image_filter = 'hot'
    print href_clean
    content_dict = {}
    category = Category.objects.get(slug=tilde_slug)
    all_images = Image.objects.filter(category=category)

    #Top/hot/new hyperlinks
    content_dict['hot_hyperlink'] = href_clean + 'hot/1/'
    content_dict['new_hyperlink'] = href_clean + 'new/1/'
    content_dict['top_hyperlink'] = href_clean + 'top/1/'

    #New images
    if image_filter == "new":
        filtered_images = Image.objects.filter(category=category).order_by('upload_date')
        content_dict['page_header'] = 'New images uploaded to ' + category.name

    #Top images
    elif image_filter == "top":
        filtered_images = Image.objects.filter(category=category).order_by('-likes')
        content_dict['page_header'] = 'Top images on all of' + category.name
    #Hot images
    else:
        current_datetime = datetime.now()
        #Gets the images in the last 12 hours and orders them by descending order
        twelve_hours_ago = current_datetime - timedelta(hours = 12)
        filtered_images = Image.objects.filter(category=category, upload_date__gte=twelve_hours_ago).order_by('-likes')
        content_dict['page_header'] = 'Popular on '+ category.name+' right now!'

    p = Paginator(filtered_images,16, allow_empty_first_page=False);

    try:
        content_dict['page_header'] = category.name
    except Category.DoesNotExist:
        content_dict['page_header'] = "This Category doesn't exist"
        return render(request,'GiggleBit/imagedisplay.html', content_dict)
    try:
        content_dict['new_images'] = p.page(page)
        if((not (p.page(page).end_index() + 1 ) /4 == 0)):
	    content_dict['not_mod4'] = 'True'
        if(p.page(page).has_next()):
            content_dict['next_page'] = href_clean + str(int(page) + 1)
	    content_dict['display_page_links'] = True
    except EmptyPage:
        if page == "1":
            content_dict['error_message'] = 'There are no images to display, sorry!'
        else:
            return redirect(href_clean + str(p.num_pages))
	if page > "1":
            content_dict['last_page'] = href_clean + str(int(page) - 1)
            content_dict['display_page_links'] = True
    return render(request,'GiggleBit/imagedisplay.html', content_dict)


#like add_page but needs to deal with multiple ~'s per image
#and is accesible from all other pages
def add_image(request):
    if request.method == 'POST':
		image_form = ImageForm(request.POST, request.FILES)
		if image_form.is_valid():
			newimage = image_form.save(commit=False)
			userobj = User.objects.get(id=request.user.id)
			currentuser = Userprofile.objects.filter(user=userobj)[0]
			newimage.uploader = currentuser
			newimage.picture = request.FILES['picture']
			newimage.upload_date = datetime.now()
			newimage.save()
			image = Image.objects.get(name=image_form.cleaned_data['name'])
                        categories = image_form.cleaned_data['category']
			for category in categories:
				image.category.add(category)

		return redirect('/gigglebit/')
    else:
        image_form = ImageForm()

    content_dict = {'image_form': image_form}
    return render(request, 'GiggleBit/addimage.html', content_dict)


#image/unique_identifier/ one for each image, need random id creator
def image(request,image_slug):
    content_dict = {}
    image = Image.objects.get(slug=image_slug)
    try:
        user = User.objects.get(id=request.user.id)
        userprofile = Userprofile.objects.get(user=user)
        if len(Liked.objects.filter(image=image,user=userprofile)) == 0:
            content_dict['not_liked'] = True
            
    except:
        pass
    content_dict['tildes'] = image.category.all()
    content_dict["image"] = image
    content_dict["comments"] = Comment.objects.filter(image=image)
    content_dict["likes_count"] = Liked.objects.filter(image=image).count()
    return render(request,"GiggleBit/image.html",content_dict)


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
    return render(request, 'GiggleBit/about.html')

def register_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        print profile_form
        if profile_form.is_valid():
            if request.user.is_authenticated():
                user = User.objects.get(id=request.user.id)
                profile = profile_form.save(commit=False)
                profile.user = user
                if 'profile_picture' in request.FILES:
                    profile.picture = request.FILES['profile_picture']
                profile.save()
        return redirect('/gigglebit/')
    else:
        form = UserProfileForm(request.GET)
        return render(request, 'GiggleBit/profile_registration.html', {'profile_form': form})


@login_required
def like_category(request):

    if request.method == 'GET':
        img = Image.objects.get(id=request.GET['image_id'])
        user = User.objects.get(id=request.GET['user_id'])
        userprofie = Userprofile.objects.get(user=user)
        likes = request.GET['likes_num']
        created = Liked.objects.get_or_create(user=userprofie,image=img)[1]
    if created:
        likes = str(int(likes)+1)
        img.likes = likes
        img.save()

    return HttpResponse(likes)

@login_required
def submit_comment(request):

    comment = request.GET['comment']
    user = Userprofile.objects.get(user=request.user)
    image = Image.objects.get(id=request.GET['image'])

    Comment.objects.create(user = user,image=image,comment=comment)

    return redirect("/gigglebit/image/" + image.slug)

def suggest_category(request):

    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_category_list(10, starts_with)

    return render(request, 'GiggleBit/cats.html', {'cat_list': cat_list})

