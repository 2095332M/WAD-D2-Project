from django import forms
from GiggleBit.models import Userprofile ,Image
from GiggleBit.models import Category
from django.template.defaultfilters import slugify

class ImageForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the image name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    category = forms.CharField(help_text="Enter tildes for this image! Like this: ~easy ~peasy ~definately ~a ~buy ")
    picture = forms.ImageField()

    class Meta:
        model = Image
        fields = ['name', 'picture', 'category',]

    def clean(self):
        cleaned_data = self.cleaned_data
        category = cleaned_data.get('category').lower()
        category = category.strip(',')
        category = category.split()
        passingtildes = []
        for tilde in category:
            if tilde[0] == '~':
                ##add to actual categories
                passingtildes.append(tilde[1:])
        allcats = Category.objects.all()

        imagecats = []
        for cats in allcats:
            if cats.name in passingtildes:
                imagecats.append(cats)
                passingtildes.remove(cats.name)
        for tildes in passingtildes:
            imagecats.append(Category.objects.create(name = tildes, views = 0))

        cleaned_data['category'] = imagecats
        return cleaned_data #plswork


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('profile_pic', 'bio')
