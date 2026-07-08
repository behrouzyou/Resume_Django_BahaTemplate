from django.db import models
from django.utils.translation import gettext_lazy as _

class GeneralSetting(models.Model):
    name=models.CharField(_('نام'),max_length=100,default='بهروز')
    title=models.CharField(_('عنوان شغل اصلی'),max_length=100,default='توسعه دهنده')
    bio=models.TextField(_('بیوگرافی'))
    location=models.CharField(_('مکان'),max_length=100,default='تهران،ایران')
    profile_image=models.ImageField(_('تصویر پروفایل'),upload_to='core/')
    resume_file=models.FileField(_('فایل رزومه'),upload_to='core/',blank=True,null=True)
    home_bg_image=models.ImageField(_('تصویر پس زمینه اصلی'),upload_to='core/')

    def __str__(self):
        return self.name
class SocialLink(models.Model):
    name=models.CharField(_('نام'),max_length=50)
    url=models.URLField(_('لینک'))
    icon_class=models.CharField(_('کلاس آیکون'),max_length=50,help_text='feb fa-github : مثال')
    setting=models.ForeignKey(GeneralSetting,on_delete=models.CASCADE,related_name='social_links')

    def __str__(self):
        return self.name
