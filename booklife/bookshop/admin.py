from django.contrib import admin
from .models import Book, Order, Comment

admin.site.register(Book)
admin.site.register(Order)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'author', 'text', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
