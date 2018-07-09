from django.contrib import admin

from .models import ProductType, Category, Attribute

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type',)
    search_fields = ('name', 'product_type')
    list_filter = ('product_type__name',)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'required')
    list_display_links = ('name', )
    search_fields = ('name', 'product_type')
    list_filter = ('product_type__name',)

admin.site.register(ProductType)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attribute, AttributeAdmin)
