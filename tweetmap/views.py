from django.http import HttpResponse
from django.shortcuts import render_to_response
from tweetmap.models import Tweet
# Create your views here.

def index(request):
  return render_to_response('map.html')
