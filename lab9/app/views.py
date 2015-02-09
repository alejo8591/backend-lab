from django.shortcuts import render, render_to_response, RequestContext

def index(request):
    return render_to_response('app_index.html', {}, context_instance=RequestContext(request))
