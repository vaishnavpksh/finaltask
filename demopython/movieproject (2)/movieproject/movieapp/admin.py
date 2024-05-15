from django.contrib import admin
from  .models import Movie,Viewusr,Deleteusr,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


admin.site.register(Movie)

admin.site.register(Viewusr)
admin.site.register(Deleteusr)

