
from django.shortcuts import render
from django.http import HttpResponse
from chess_website.utils.helpers import getData

# Create your views here.
def openings(request):
    return render(request, 'chess_website/index.html')

def profile(request):
    if request.POST.get('name'):
        info = getData(request.POST.get("name"))
        if info:
            return render(request, 'chess_website/profile.html', 
                      {'year': info['year'], 'country': info['country'], 'ratings':info['ratings']})
        else:
            return render(request, 'chess_website/profile.html',
                           {'error': 'There was an error, retry.'})
    else:
        return render(request, 'chess_website/profile.html')
    
def index(request):
    if request.POST.get('name'):
        info = getData(request.POST.get("name"))
        if info:
            return render(request, 'chess_website/profile.html', 
                      {'year': info['year'], 'country': info['country'], 'ratings':info['ratings']})
        else:
            return render(request, 'chess_website/profile.html',
                           {'error': 'There was an error, retry.'})
    else:
        return render(request, 'chess_website/profile.html')

