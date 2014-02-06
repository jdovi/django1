from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Function to send / request to the index page
def index(request):
	return render_to_response('index.html')