from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .utils import get_follower

class Twitter(View):

    def get(self, request):
        return render(request, "home.html")
        
    def post(self, request):
        url = request.POST.get('twitter_url')
        if not url:
            return render(request, "home.html", {'state':'0'})
        data, name = get_follower(url)
        if name:
            context = {'name':name, 'handle':url.split('/')[-1], 'message':data}
        else:
            context = {'name':None, 'handle':None, 'message':data}
        return render(request, "home.html", context)
