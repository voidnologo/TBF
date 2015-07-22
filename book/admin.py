from django.contrib import admin

from .models import Article, Source, Author


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ['author', 'source']
    search_fields = ['title', 'author', 'source']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Source)
