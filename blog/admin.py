from django.contrib import admin

# Register your models here.

from .models import Category,Tag,Blog

class CategoryInline(admin.TabularInline):
	model = Category.name

#class TagInline(admin.TabularInline):
#	model = Tag.id

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name']
	list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
	fields = ['name']
	list_display = ('name',)

class TagInline(admin.StackedInline):
	model = Tag.name
	filter_horizontal = ('tags',)

class BlogAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':('title','author','content','created','category','tags',)}),
	]
	list_display = ('title','author','created',)
	search_fields = ['title']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
#admin.site.register(Blog)





