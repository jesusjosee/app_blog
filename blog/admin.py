from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post) # this funtion make the same of admin.site.register
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display= ('title', 'slug', 'author', 'publish', 'status')
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields = {'slug':('title',)} #autocomplete the slug flied
    raw_id_fields= ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')



# <----this proces is with admin.site.register()---->

#class PostAdmin(admin.ModelAdmin):
#    readonly_fields=('created','updated')

#admin.site.register(Post, PostAdmin)