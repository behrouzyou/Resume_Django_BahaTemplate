from django.db import models
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    DISPLAY_TYPE_CHOICES = [('progress', 'Progress Bar') , ('chart' , 'Chart')]
    name = models.CharField(_('نام مهارت'),max_length=50)
    percentage = models.PositiveIntegerField(_('درصد تسلط'),default=80)
    display_type = models.CharField(_('نوع مهارت'),max_length=10,choices=DISPLAY_TYPE_CHOICES,default='progress')

    class Meta:
        ordering = ['-percentage']

    def __str__(self):
        return self.name

class ResumeEntry(models.Model):
    ENTRY_TYPE_CHOICES = [('experience','سوابق کاری'),('education','سوابق تحصیلی')]
    entry_type = models.CharField(_('نوع'),max_length=20,choices=ENTRY_TYPE_CHOICES)
    title = models.CharField(_('عنوان'),max_length=200)

    start_year = models.PositiveIntegerField(_('سال شروع'),null=True,blank=True)
    end_year = models.PositiveIntegerField(_('سال پایان'),null=True,blank=True)

    company_or_field = models.CharField(_('نام شرکت / رشته'),max_length=200,null=True,blank=True)


    description = models.TextField(_('توضیحات'))

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f'{self.get_entry_type_display()} {self.title}'


class WorkProcess(models.Model):
    step = models.PositiveIntegerField(_('مرحله'))
    title = models.CharField(_('عنوان'),max_length=200)
    description = models.TextField(_('توضیحات'))

    class Meta:
        ordering = ['-step']

    def __str__(self):
        return f'مرحله {self.step} - {self.title}'
