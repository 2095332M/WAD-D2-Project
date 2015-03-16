from django import template
from GiggleBit.models import Category, User

register = template.Library()

@register.inclusion_tag('gigglebit/cats.html')
def get_category_list():
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


