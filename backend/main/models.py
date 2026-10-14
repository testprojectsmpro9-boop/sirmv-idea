from django.db import models
from django.utils import timezone

class IdeaSubmission(models.Model):
    CATEGORY_CHOICES = [
        ('school', 'School (8th - 12th Std)'),
        ('college', 'College (UG / PG)'),
    ]
    
    full_name = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=300)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    project_title = models.CharField(max_length=160)
    description = models.TextField(max_length=4000)
    supporting_document = models.FileField(upload_to='submissions/', blank=True, null=True)
    submitted_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Idea Submission'
        verbose_name_plural = 'Idea Submissions'
    
    def __str__(self):
        return f"{self.project_title} by {self.full_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"Message from {self.name} - {self.email}"


class CollaborationInquiry(models.Model):
    COLLABORATION_CHOICES = [
        ('partner', 'Partner'),
        ('mentor', 'Mentor'),
        ('sponsor', 'Sponsor'),
    ]
    
    organization_name = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=200)
    work_email = models.EmailField()
    collaboration_type = models.CharField(max_length=20, choices=COLLABORATION_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Collaboration Inquiry'
        verbose_name_plural = 'Collaboration Inquiries'
    
    def __str__(self):
        return f"{self.organization_name} - {self.collaboration_type}"
