from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Comment
    extra = 3


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author Details', {'fields': ['author',]}),
        ('Text Details', {'fields': ['title', 'text']}),
        ('Date information', {'fields': ['create_date', 'published_date']}),
    ]

    inlines = [ChoiceInLine]

    list_filter = ['create_date']

    search_fields = ['title']


admin.site.register(Post, PostAdmin)


