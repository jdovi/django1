from django.contrib import admin
from notify.models import Waiter

# Register your models here.
class WaiterAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields':['customer']}),
		('Vehicle information',	{'fields': ['vYear','vMake','vModel'], 'classes':['collapse']}),

	]
	list_display = ('customer', 'vYear', 'vModel')

admin.site.register(Waiter, WaiterAdmin)