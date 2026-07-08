from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    name = models.CharField(_('نام'), max_length=100)
    email = models.EmailField(_('ایمیل'))
    note = models.TextField(_('متن پیام'))

    created_at = models.DateTimeField(_('تاریخ ارسال'), auto_now_add=True)
    is_read = models.BooleanField(_('خوانده شده ؟'), default=False)

    def __str__(self):
        return f'{self.name} - {self.email}'
