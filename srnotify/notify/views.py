from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from notify.models import Waiter

# Function to send / request to the index page
def index(request):
	#return render_to_response('index.html')
	customer_list = Waiter.objects.all()
	#output = ','.join([p.customer for p in customer_list])
	
	context = {'customer_list': customer_list,}
	return render(request, 'notify/index.html', context)
	
def detail(request, customer):
	return HttpResponse("You're looking at the notify %s." % customer)
	
def results(request, customer):
	return HttpResponse("You're looking at the results of notify %s." % customer)
	
def vote(request, customer):
	return HttpResponse("You're voting on nofity %s." % customer)