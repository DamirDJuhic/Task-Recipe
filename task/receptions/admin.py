from django.contrib import admin
from .models import Rating, Reception, Writter,Ingredient


admin.site.register(Writter)
admin.site.register(Rating)

class IngredientInline(admin.TabularInline):
    model = Ingredient

@admin.register(Reception)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, ]