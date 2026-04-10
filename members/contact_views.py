from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

@csrf_exempt
def contact_form(request):
    """Handle contact form submission and send email"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            
            # Create email subject
            email_subject = f'New Contact Form Submission: {subject}'
            
            # Create email body
            email_body = f"""
Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}

---
This message was sent from Avin Shukri Pharmaceuticals Contact Form
            """
            
            # Send email to company
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL, settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            # Send confirmation email to user
            confirmation_subject = 'Thank you for contacting Avin Shukri Pharmaceuticals'
            confirmation_body = f"""
Dear {name},

Thank you for contacting Avin Shukri Pharmaceuticals Private Limited. We have received your message regarding "{subject}" and will get back to you shortly.

Your Message:
{message}

Our team will review your inquiry and respond within 24-48 business hours.

Best regards,
Team Avin Shukri Pharmaceuticals
📞 +91 9500804839
📧 info@avinshukri.com
🌐 www.avinshukri.com
            """
            
            send_mail(
                subject=confirmation_subject,
                message=confirmation_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Message sent successfully! We will contact you soon.'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error sending message: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })

def contact(request):
    """Contact page view"""
    return render(request, 'contact.html')
