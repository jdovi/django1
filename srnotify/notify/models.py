from django.db import models

# Definition of the waiter class
class Waiter(models.Model):
	customer = models.CharField(max_length=100)
	vYear = models.IntegerField()
	vMake = models.CharField(max_length=25)
	vModel = models.CharField(max_length=25)
	status = models.CharField(max_length=10)
	hatnum = models.CharField(max_length=1)
	
	#return customer name when calling the class.object.all()
	def __unicode__(self):
		return self.customer