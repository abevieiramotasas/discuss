# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def main(request):
   return render_to_response('index.html', {}, context_instance=RequestContext(request))

def server_side(request):
   code = request.GET.get('code', None)
   if not code:
      dialog_url = "https://www.facebook.com/dialog/oauth?client_id=" + settings.FACEBOOK_APP_ID + "&redirect_uri=" + settings.FACEBOOK_MY_URL
      dados = {}
      dados['dialog_url'] = dialog_url
      return render_to_response('base.html', dados, context_instance=RequestContext(request))
