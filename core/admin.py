from django.contrib import admin
from .models import GeneralSetting , SocialLink

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('name' , 'title','location')
    search_fields = ('name','title')

    fieldsets = (
        ('اطلاعات اصلی',{
            'fields' : ('name','title','bio','location','profile_image','resume_file')
        }),

        ('تنظیمات صفحه اصلی', {
            'fields': ('home_bg_image',)
        }),

        ('هدر سایت',{
            'fields':('logo','enable_sound')
        }),
    )

    inlines = [SocialLinkInline]




@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name' , 'url','icon_class','setting')
    search_fields = ('name',)




