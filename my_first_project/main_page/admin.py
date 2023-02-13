from django.contrib import admin 
from .models import Category, Dish

# Register your models here.
class DishAdmin(admin.TabularInline):
    model = Dish #state model for which we created connection 
    raw_id_fields = ['category'] 
    # state attribute from <model.py> which provides connection to class Category

@admin.register(Category) # <Category> - model to which the class will be addicted  
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [DishAdmin] # state class which is built-in the current class

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish 
    # make a list of all dishes - data collected from Category
    list_display = ['title', 'position', 'is_visible','price', 'category','is_special']
    list_editable = ['position', 'is_visible', 'price', 'category','is_special']
    list_filter = ['category', 'is_special', 'is_visible'] # add filter to admin dashboard

# admin.site.register(Category)
# admin.site.register(Dish)


    

