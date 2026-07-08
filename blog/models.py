from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class BlogCategory(models.Model):
    name = models.CharField(_('نام دسته'), max_length=50)
    slug = models.SlugField(_('آدرس یکتا'), unique=True, allow_unicode=True, null=True, blank=True)

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')

    def __str__(self): return self.name


class Tag(models.Model):
    name = models.CharField(_('نام برچسب'), max_length=50)
    slug = models.SlugField(_('آدرس یکتا'), unique=True, allow_unicode=True,null=True,blank=True)


    class Meta:
        verbose_name = _('برچسب')
        verbose_name_plural = _('برچسب ها')

    def __str__(self): return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name=_('نویسنده'),null=True,blank=True)
    title = models.CharField(_('عنوان پست'), max_length=200)
    slug = models.SlugField(_('آدرس یکتا'), unique=True, allow_unicode=True,null=True,blank=True)
    image = models.ImageField(_('تصویر'), upload_to='blog/')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, verbose_name=_('دسته بندی'),
                                 related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_('برچسب ها'), related_name='posts')
    created_at = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    content = models.TextField(_('محتوا'), blank=True)
    updated_at = models.DateTimeField(_('تاریخ بروز رسانی'), auto_now=True)
    is_active = models.BooleanField(_('فعال'), default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('پست')
        verbose_name_plural = _('پست ها')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_('پست'))
    name = models.CharField(_('نام'), max_length=50)
    email = models.EmailField(_('ایمیل'))
    message = models.TextField(_('پیام'))
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(_('تایید شده'), default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies',
                               verbose_name=_('والد'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('دیدگاه')
        verbose_name_plural = _('دیدگاه ها')


    def __str__(self):
        return f'{self.name} - {self.post.title}'
