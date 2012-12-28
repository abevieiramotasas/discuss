from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
   views = []
   views.append('autoescape')
   views.append('cycle')   
   views.append('debug')

   return render_to_response('tag_index.html', {'views': views}, context_instance=RequestContext(request))

def autoescape(request):
   html = r"""
	<div style="background-color:red">
		Com fundo vermelho
	</div>
	"""

   return render_to_response('autoescape.html', {'html': html}, context_instance=RequestContext(request))

def cycle(request):
   valores = [x for x in range(0, 20)]
   return render_to_response('cycle.html', {'valores': valores}, context_instance=RequestContext(request))

def debug(request):
   return render_to_response('debug.html', {}, context_instance=RequestContext(request))
