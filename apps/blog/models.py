from django.db import models
from django.utils.translation import gettext_lazy as _
from django_restful_translator.models import TranslatableModel


class Categories(models.Model):
    name = models.CharField(_("Category name"), max_length=500, null=True, blank=True)

    translatable_fields = ['name']

    objects = models.Manager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Kategoriyalar")
        db_table = 'categories'


class Blog(models.Model):
    title = models.CharField(_('Title'), max_length=500, null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    is_seen = models.IntegerField(default=0, verbose_name="Is Seen")
    category = models.ManyToManyField(Categories, null=True, blank=True,
                                      related_name="Category", verbose_name=_('Choose category'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("Published date"))

    translatable_fields = ['title', 'description']

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Bloglar")
        ordering = ['created_at']
        db_table = 'blog'


class BlogImage(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=_("Image"))
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="blogImage",
                             verbose_name=_('Bloglar'))

    def __str__(self):
        return self.blog.title

    objects = models.Manager()

    class Meta:
        verbose_name = _("Blog image")
        verbose_name_plural = _("Blog Rasmlari")
        db_table = 'blog_image'


class BlogComment(models.Model):
    full_name = models.CharField(_("To'liq ism familiyasi"), max_length=250, null=True, blank=True)
    phone = models.CharField(_("Telefon raqami"), max_length=250, null=True, blank=True)
    comment = models.TextField(verbose_name="Izoh", null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name="blogCommant",
                             verbose_name=_('Bloglar'))

    objects = models.Manager()

    class Meta:
        verbose_name = _("Blog Komment")
        verbose_name_plural = _("Blog Kommentlar")
        db_table = 'blog_comment'
