from django.contrib import admin
from gallery.models import Album, Photo, Keywords


class AlbumInLine(admin.StackedInline):
    model = Photo
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    fields = ['album_name','albums_img', 'keywords']
    inlines = [AlbumInLine]

#class Albumfoto (admin.ModelAdmin):
    #fields = ['file_foto']


#class PhotoAdmin(admin.ModelAdmin):
   #fields = ['name', 'album', 'file', 'location']
  
class TagsAdmin (admin.ModelAdmin):
    fields = ['tag']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Keywords, TagsAdmin)
