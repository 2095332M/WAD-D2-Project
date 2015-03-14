from django import forms
from GiggleBit.models import Image

class ImageForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the image name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Image
        fields = ('name', 'picture', 'category',)
