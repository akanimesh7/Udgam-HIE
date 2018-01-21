from django.contrib import admin
from .models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','image','category','price','stock','available','updated']
    list_filter=['available','created','updated','category']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,ProductAdmin)

