from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Categories, Blog, BlogImage, BlogComment
from django_restful_translator.admin import TranslationInline

class ImageMixin:
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="150" />')
        return ""
    image_tag.short_description = 'Image'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class BlogImageInline(admin.StackedInline, ImageMixin):
    model = BlogImage
    extra = 1
    readonly_fields = ('image_tag',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('is_seen', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'category')
    ordering = ('-created_at',)
    inlines = [BlogImageInline]

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"


class BlogImageAdmin(admin.ModelAdmin, ImageMixin):
    list_display = ('blog', 'image_tag')
    search_fields = ('blog__title',)
    readonly_fields = ('image_tag',)

    class Meta:
        verbose_name = "Blog Rasm"
        verbose_name_plural = "Blog Rasmlar"


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone']
    search_fields = ['full_name']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = _("OzodBobo")
admin.site.site_title = _("Admin Portal")
admin.site.index_title = _("Maxsus boshqaruv paneliga xush kelibsiz")
