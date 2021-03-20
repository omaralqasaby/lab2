from django.contrib import admin
from .models import Movie,Category,Country,Rate
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
   list_display=("title","year","rate")
   list_filter=("year",)

class MovieInLine(admin.StackedInline):
    model=Movie
    extra=2
    max_num=10
class countryAdmin(admin.ModelAdmin):
    inlines=[MovieInLine]

admin.site.register(Movie,MovieAdmin)
admin.site.register(Category)
admin.site.register(Country,countryAdmin)
admin.site.register(Rate)