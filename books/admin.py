from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pages', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'author', 'description')
    list_editable = ('category', 'pages')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'author', 'category')
        }),
        ('Описание', {
            'fields': ('description', 'image')
        }),
        ('Техническая информация', {
            'fields': ('pages', 'created_at')
        }),
    )
