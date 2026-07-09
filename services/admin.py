from django.contrib import admin
from .models import Service ,PricingPlan,Testimonial,ExperienceBox,Interest
# Register your models here.


admin.site.register([Service,Interest,PricingPlan,Testimonial,ExperienceBox])
