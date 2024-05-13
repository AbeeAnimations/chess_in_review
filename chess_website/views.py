
from django.shortcuts import render
from django.http import HttpResponse
from chess_website.utils.helpers import getProfile, getOpenings

# Views
def index(request):
    return render(request, 'chess_website/index.html')


def profile(request):
    if request.POST.get('name'):
        info = getProfile(request.POST.get("name"))
        if info:
            return render(request, 'chess_website/profile.html', 
                      {'year': info['year'], 'country': info['country'], 'ratings':info['ratings'], 'name':info['name']})
        else:
            return render(request, 'chess_website/profile.html',
                           {'error': 'There was an error, retry.'})
    else:
        return render(request, 'chess_website/profile.html')
    
def openings(request):
    if request.POST.get('name'):
        info = getOpenings(request.POST.get("name"))
        if info:
            return render(request, 'chess_website/openings.html', 
                      {'top_5': info['top_5']})
        else:
            return render(request, 'chess_website/openings.html',
                           {'error': 'There was an error, retry.'})
    else:
        return render(request, 'chess_website/openings.html')

