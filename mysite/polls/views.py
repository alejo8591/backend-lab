from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = RequestContext(request, {
			'latest_poll_list' : latest_poll_list,
		})
	return render(request, 'index.html', context)

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404

	return render(request, 'detail.html', {'poll':poll})

def results(request, poll_id):
	return HttpResponse("Your looking result of polls %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s" %poll_id)