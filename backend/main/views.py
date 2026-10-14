from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import IdeaSubmission, ContactMessage, CollaborationInquiry

def home(request):
    """Home page with featured innovations"""
    featured_ideas = IdeaSubmission.objects.all()[:4]
    
    # Statistics
    total_ideas = IdeaSubmission.objects.count()
    school_entries = IdeaSubmission.objects.filter(category='school').count()
    college_entries = IdeaSubmission.objects.filter(category='college').count()
    institutions = IdeaSubmission.objects.values('institution_name').distinct().count()
    
    context = {
        'featured_ideas': featured_ideas,
        'total_ideas': total_ideas,
        'school_entries': school_entries,
        'college_entries': college_entries,
        'institutions': institutions,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About Sir MV page"""
    return render(request, 'main/about.html')

def guidelines(request):
    """Official rules and guidelines for students, schools, and group participants."""
    return render(request, 'main/guidelines.html')



def idea_submission_form(request):
    """Serve the official DOCX form so browsers/devices can open it from the server."""
    form_path = Path(settings.PROJECT_ROOT) / 'frontend' / 'static' / 'media' / 'guidelines' / 'sirmv.docx'

    if not form_path.exists():
        raise Http404('Idea submission form not found.')

    return FileResponse(
        form_path.open('rb'),
        as_attachment=False,
        filename='sirmv-idea-submission-form.docx',
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    )


def ideathon(request):
    """Ideathon page with all submissions"""
    filter_category = request.GET.get('category', 'all')
    
    if filter_category == 'school':
        ideas = IdeaSubmission.objects.filter(category='school')
    elif filter_category == 'college':
        ideas = IdeaSubmission.objects.filter(category='college')
    else:
        ideas = IdeaSubmission.objects.all()
    
    context = {
        'ideas': ideas,
        'filter_category': filter_category,
    }
    return render(request, 'main/ideathon.html', context)

def submit_idea(request):
    """Idea submission form"""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        institution_name = request.POST.get('institution_name')
        category = request.POST.get('category')
        project_title = request.POST.get('project_title')
        description = request.POST.get('description')
        supporting_document = request.FILES.get('supporting_document')
        
        idea = IdeaSubmission(
            full_name=full_name,
            institution_name=institution_name,
            category=category,
            project_title=project_title,
            description=description,
            supporting_document=supporting_document
        )
        idea.save()
        
        messages.success(request, 'Your idea has been submitted successfully!')
        return redirect('ideathon')
    
    # Pre-fill category if provided in URL
    category = request.GET.get('category', '')
    context = {'category': category}
    return render(request, 'main/submit.html', context)

def contact(request):
    """Contact page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact_msg = ContactMessage(
            name=name,
            email=email,
            message=message
        )
        contact_msg.save()
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'main/contact.html')

def collaboration(request):
    """Collaboration page"""
    if request.method == 'POST':
        organization_name = request.POST.get('organization_name')
        contact_person = request.POST.get('contact_person')
        work_email = request.POST.get('work_email')
        collaboration_type = request.POST.get('collaboration_type')
        message = request.POST.get('message')
        
        inquiry = CollaborationInquiry(
            organization_name=organization_name,
            contact_person=contact_person,
            work_email=work_email,
            collaboration_type=collaboration_type,
            message=message
        )
        inquiry.save()
        
        messages.success(request, 'Your inquiry has been submitted successfully!')
        return redirect('collaboration')
    
    return render(request, 'main/collaboration.html')


def about_us(request):
    """About Us — platform & team page"""
    return render(request, 'main/about_us.html')


def events(request):
    """Events page — upcoming & past events"""
    return render(request, 'main/events.html')


def gallery(request):
    """Gallery page — image showcase"""
    return render(request, 'main/gallery.html')
