from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(_('عنوان خدمت'),max_length=100)
    description = models.TextField(_('توضیحات'))
    icon_class = models.CharField(_('کلاس آیکون'),max_length=50,help_text='مثال : fas fa-desktop')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
