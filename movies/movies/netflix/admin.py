from django.contrib import admin
from .models import Movie,Country,Rate, Category
# Register your models here.
class MovieIline(admin.TabularInline):
    model=Movie
    extra=1
    max_num=10
class CategoryAdmin(admin.ModelAdmin):
    inlines=[MovieIline]


class MovieAdmin(admin.ModelAdmin):
    list_display=("name","overview","year")
    list_filter=("year",)

    
admin.site.register(Movie,MovieAdmin)
admin.site.register(Country,CategoryAdmin)
admin.site.register(Rate)
admin.site.register(Category)