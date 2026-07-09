from django.shortcuts import render , redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage
from django.views.decorators.http import require_POST
from django.http import JsonResponse


@require_POST
def contact_submit(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if not is_ajax:
        return JsonResponse({'success':False , 'message':'درخواست نامعتبر'},status=400)

    form = ContactForm(request.POST)



    if form.is_valid():
        contact = form.save()

        user_name = form.cleaned_data['name']
        user_email = form.cleaned_data['email']
        user_note = form.cleaned_data['note']



        try:
            subject = 'پیام شما با موفقیت ارسال شد'

            html_message = render_to_string('emails/contact_user.html', {'name':user_name, })

            plain_message = f"""

            سلام {user_name} ،عزیز
            پیام شما با موفقیت دریافت شد.
            در اسرع وقت به پیام شما پاسخ داده خواهد شد.

            باشکر از تماس شما


            """

            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
                html_message=html_message,
                fail_silently=False,
            )

            admin_subject = f'پیام جدید از طرف {user_name}'
            admin_message = f"""

            پیام جدید در سایت ثبت شد:
            نام:{user_name}
            ایمیل:{user_email}
            پیام: {user_note}
            تاریخ:{contact.created_at}
            """

            send_mail(
                subject=admin_subject,
                message=admin_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )

            return JsonResponse({
                'success':True,
                'message':'پیام شما با موفقیت ارسال شد.'
            })


        except Exception as e:
            print(f'خطا در ارسال ایمیل {e}')
            return JsonResponse({
                'success':True,
                'message':'پیام شما با موفقیت ارسال شد(ایمیل ارسال نشد).'
            })

    else:
        errors = []
        for field , error_list in form.errors.items():
            errors.append(f'{field}:{error_list[0]}')

        return JsonResponse({
            'success': False,
            'message': 'لطفا اطلاعات را به درستی وارد کنید',
            'errors':errors,
        })
