from django import template
from core.models import GeneralSetting
from services.models import ExperienceBox,Service,Interest,Testimonial,PricingPlan

register=template.Library()
@register.inclusion_tag('partials/_header_nav.html')
def site_header():
    setting=GeneralSetting.objects.first()
    return{
        'setting':setting
    }
@register.inclusion_tag('partials/about/_personal_info.html')
def personal_info():
    settings=GeneralSetting.objects.first()
    return {'setting':settings}

@register.inclusion_tag("partials/about/_experience_boxes.html")
def experience_boxes():


    return {
        "boxes":ExperienceBox.objects.all() ,

    }
@register.inclusion_tag("partials/about/_interest.html")
def interest():


    return {
        "interest":Interest.objects.all() ,

    }

@register.inclusion_tag("partials/about/_services.html")
def services():


    return {
        "services":Service.objects.all() ,

    }

@register.inclusion_tag("partials/about/_testimonial.html")
def testimonials():


    return {
        "item":Testimonial.objects.all() ,

    }

@register.inclusion_tag("partials/about/_pricing.html")
def pricing_plan():


    return {
        "plans":PricingPlan.objects.all() ,

    }
