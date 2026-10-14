from django.contrib import admin
from .models import IdeaSubmission, ContactMessage, CollaborationInquiry

@admin.register(IdeaSubmission)
class IdeaSubmissionAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'full_name', 'institution_name', 'category', 'submitted_at']
    list_filter = ['category', 'submitted_at']
    search_fields = ['project_title', 'full_name', 'institution_name', 'description']
    date_hierarchy = 'submitted_at'
    readonly_fields = ['submitted_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['name', 'email', 'message']
    date_hierarchy = 'submitted_at'
    readonly_fields = ['submitted_at']

@admin.register(CollaborationInquiry)
class CollaborationInquiryAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'contact_person', 'work_email', 'collaboration_type', 'submitted_at']
    list_filter = ['collaboration_type', 'submitted_at']
    search_fields = ['organization_name', 'contact_person', 'work_email', 'message']
    date_hierarchy = 'submitted_at'
    readonly_fields = ['submitted_at']
