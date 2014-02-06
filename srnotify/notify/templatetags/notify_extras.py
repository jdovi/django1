from django import template
register = template.Library()

def is_odd(num):
	if num % 2 != 0:
		result=True
	else:
		result=False
	
	
	return result