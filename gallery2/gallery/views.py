from django.shortcuts import render
from gallery.models import Album, Photo, Keywords
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, context, Template
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpRequest
from datetime import datetime

# Create your views here.
def albums (request):
    args ={}
    args.update (csrf(request))
    args['albums']=Album.objects.all()
    args ['year'] = datetime.now().year
    return render_to_response ('albums.html', args)


def album (request, album_id=1):
    args ={}
    args.update (csrf(request))
    
    args['photos']=Photo.objects.filter(album_id=album_id)
    args ['year'] = datetime.now().year
    return render_to_response ('album.html', args)


def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title':'I am in social networking service:',
            'message':'',
            'year':datetime.now().year,
        }
    )
