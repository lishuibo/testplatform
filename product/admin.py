from django.contrib import admin
from product.models import Product
from apitest.models import Apis
from apptest.models import Appcase
from webtest.models import Webcase
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'apitest']
    model = Apis
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [ApisAdmin]


class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename', 'apptestresult', 'create_time', 'id', 'product']
    model = Appcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [AppcaseAdmin]


class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult', 'create_time', 'id', 'product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [WebcaseAdmin]

admin.site.register(Product, ProductAdmin)

