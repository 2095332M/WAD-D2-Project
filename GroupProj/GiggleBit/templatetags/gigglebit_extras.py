from django import template
from GiggleBit.models import Category, User

register = template.Library()

##@register.inclusion_tag('GiggleBit/catlist.html')
##def get_category_list(max_results=0, starts_with=''):
##    cat_list = []
##    if starts_with:
##        cat_list = Category.objects.filter(name__istartswith=starts_with)
##
##
##    if max_results > 0:
##        if len(cat_list) > max_results:
##            cat_list = cat_list[:max_results]
##            
##    return cat_list

@register.inclusion_tag('GiggleBit/cats.html')
def get_all_cats():
    return {'cats': Category.objects.all()}

@register.inclusion_tag('gigglebit/favcats.html')
def get_fav_cats():
#doesnt work for shit
##    user = User.objects.get(id=request.user.id)
##    c = Category.objects.filter(user=user)
##    catlist = []
##    for cats in c:
##        catlist.append(cats.category)
##    return {'cats': Category.objects.filter(user=user)}
    return []
