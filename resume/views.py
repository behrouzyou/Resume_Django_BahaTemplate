from django.shortcuts import render
from .models import ResumeEntry, Skill, WorkProcess

def resume_view(request):
    experience_list = ResumeEntry.objects.filter(entry_type='experience')
    education_list = ResumeEntry.objects.filter(entry_type='education')
    skills = Skill.objects.all()
    work_process = WorkProcess.objects.all()

    return render(request, 'partials/_resume_page.html', {
        "experience_list": experience_list,
        "education_list": education_list,
        "skills": skills,
        "work_process": work_process,
    })
     