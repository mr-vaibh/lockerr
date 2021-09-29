from django.forms import ModelForm

from .models import LongUrl

class UrlForm(ModelForm):
    class Meta:
        model = LongUrl
        fields = ['url', 'description']