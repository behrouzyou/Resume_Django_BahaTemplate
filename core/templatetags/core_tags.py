from django import template
from core.models import GeneralSetting
from services.models import ExperienceBox,Service,Interest,Testimonial,PricingPlan
from resume.models import ResumeEntry, Skill, WorkProcess
from projects.models import ProjectCategory,Project
from django.contrib import messages
from django.conf import settings
from contact.forms import ContactForm
from blog.models import Post



register=template.Library()
@register.inclusion_tag('partials/_header_nav.html')
def site_header():
    setting=GeneralSetting.objects.first()
    return{
        'setting':setting
    }

#     SERVICES TAG
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
#           RESUME TAG
@register.inclusion_tag('partials/_experience_list.html')
def resume_experience():
    # فقط سوابق کاری
    items = ResumeEntry.objects.filter(entry_type='experience')
    return {"items": items}

@register.inclusion_tag('partials/_education_list.html')
def resume_education():
    # فقط سوابق تحصیلی
    items = ResumeEntry.objects.filter(entry_type='education')
    return {"items": items}

@register.inclusion_tag('partials/_skills_list.html')
def resume_skills():
    skills = Skill.objects.all().order_by('-percentage')
    return {"skills": skills}

@register.inclusion_tag('partials/_work_process.html')
def resume_work_process():
    process_list = WorkProcess.objects.all().order_by('step')
    return {"process_list": process_list}


#   PROJECT AG
@register.inclusion_tag("partials/_portfolio_page.html")
def project_list():
    categories=ProjectCategory.objects.all()
    projects=Project.objects.all()

    return {
        "categories": categories,
        'projects':projects,

    }

#   CONTACT TAG
@register.inclusion_tag('tags/contact_form.html',takes_context=True)
def contact_section(context):
    request = context['request']
    form = ContactForm()

    message_list = messages.get_messages(request)

    return {
        'form': form,
        'request': request,
        'messages': message_list,
    }

@register.simple_tag
def get_contact_info():
    return {
        'email':getattr(settings, 'CONTACT_EMAIL', 'behrouzyou@gmail.com'),
        'phone':getattr(settings,'CONTACT_PHONE','(+98) 9373007494'),
        'address':getattr(settings,'CONTACT_ADDRESS','ورامین کوچه دوم')
    }

#              BLOG TAG
@register.inclusion_tag('partials/_blog_page.html')
def latest_blog_posts(count=5):
    posts = Post.objects.filter(is_active=True).order_by('created_at')[:count]
    return {'posts': posts}
