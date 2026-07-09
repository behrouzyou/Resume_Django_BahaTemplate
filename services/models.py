from django.db import models
from django.utils.translation import gettext_lazy as _


class ExperienceBox(models.Model):
    title = models.CharField(_('عنوان'),max_length=100)
    icon_class = models.CharField(_('کلاس آیکون'),max_length=50,help_text='مثال : fas fa-desktop')
    subtitle = models.CharField(_('زیر عنوان'),max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(_('عنوان'),max_length=100)
    icon_class = models.CharField(_('کلاس آیکون'),max_length=50,help_text='مثال : fas fa-desktop')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title





class Service(models.Model):
    title = models.CharField(_('عنوان خدمت'),max_length=100)
    description = models.TextField(_('توضیحات'))
    icon_class = models.CharField(_('کلاس آیکون'),max_length=50,help_text='مثال : fas fa-desktop')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(_('نام'),max_length=100)
    job_title = models.CharField(_('عنوان شغلی'),max_length=100)
    image = models.ImageField(_('عکس'),upload_to='testimonial/')
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField(_('نظر'))

    def __str__(self):
        return self.name

class PricingPlan(models.Model):
    title = models.CharField(_('عنوان'),max_length=100)
    icon_class = models.CharField(_('کلاس آیکون'),max_length=50,help_text='مثال : fas fa-desktop')
    price = models.CharField(_('قیمت'),max_length=25)
    period = models.CharField(_('بازه زمانی'),max_length=50,default='ماهانه')
    features = models.TextField(_('ویژگی ها (هر خط یک مورد)'))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def feature_list(self):
        return self.features.split('\n')

    def __str__(self):
        return self.title
