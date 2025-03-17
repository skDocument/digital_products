from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(_('text'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='categories/')
    is_enabled = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)


    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Product(models.Model):
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='products/')
    is_enabled = models.BooleanField(_('is enabled'),default=True)
    categories = models.ManyToManyField("Category",verbose_name=_('categories'),blank=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

class Files(models.Model):
    products = models.ForeignKey('Product',verbose_name=_('products'),on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    file = models.FileField(_('file'),upload_to='files/%Y/%m/%d')
    is_enabled = models.BooleanField(_('is enabled'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')