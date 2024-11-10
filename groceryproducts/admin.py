from django.contrib import admin
from groceryproducts.models import category, Grocery, Product, Cart, CartItem


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ('category_img','category_title')
    
admin.site.register(category,categoryAdmin)  

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')

admin.site.register(Grocery,GroceryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('product_img','product_title','product_price')
admin.site.register(Product, productAdmin)    

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_product_titles')

    def get_product_titles(self, obj):
        return ", ".join([p.product_title for p in obj.products.all()])
    get_product_titles.short_description = "Product Titles"

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product','cart','quantity')
admin.site.register(CartItem, CartItemAdmin)    