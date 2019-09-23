from django.contrib import admin
from testapp.models import cropdetail,irrigation,Userphone
class Cropadmin(admin.ModelAdmin):
	list_display=['name','cropname','cropquantity']
admin.site.register(cropdetail,Cropadmin)
class IrrigationAdmin(admin.ModelAdmin):
	list_display=['CropStage']
admin.site.register(irrigation,IrrigationAdmin)
class UserphoneAdmin(admin.ModelAdmin):
	list_display=['phoneno']
admin.site.register(Userphone,UserphoneAdmin)