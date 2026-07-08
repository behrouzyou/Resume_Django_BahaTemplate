from django.db import models
from django.utils.translation import gettext_lazy as _


class ProjectCategory(models.Model):
    name = models.CharField(_('نام دسته بندی'),max_length=50)
    slug = models.SlugField(_('اسلاگ (برای فیلتر)'),unique=True,help_text='مثال : یک کلمه انگلیسی برای استفاده در فیلتر')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(_('عنوان پروژه'),max_length=200)
    image = models.ImageField(_('تصویر'),upload_to='projects/')
    category = models.ForeignKey(ProjectCategory,on_delete=models.SET_NULL,null=True,related_name='projects')

    def __str__(self):
        return self.title


