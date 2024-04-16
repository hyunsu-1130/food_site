from django.contrib import admin
from chinese.models import Category, Food

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
  list_display = ('category', 'name', 'price', 'description', 'image_url')