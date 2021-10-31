from django.contrib import admin
from myapp.models import acc_details
class bankdetails(admin.ModelAdmin):
    list_display=['name','account_num','ifsc','mob_no','location','amount']
admin.site.register(acc_details,bankdetails)
