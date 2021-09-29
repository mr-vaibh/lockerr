from django.shortcuts import render, redirect

from .models import LongUrl
from .forms import UrlForm

# Create your views here.

def index(request):
    context = {}

    if request.method == 'POST':
        url = request.POST['url']
        description = request.POST.get('description', '')

        # Check if url is valid
        if not (url[:7] == 'http://' or url[:8] == 'https://'):
            url = 'http://' + url

        long_url = LongUrl(url=url, description=description)
        long_url.save()
        
        context['slug'] = long_url.slug
    
    return render(request, 'main/index.html', context)


def long_url(request, long_url):
    obj = LongUrl.objects.get(slug=long_url)
    return redirect(obj.url)