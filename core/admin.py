from django.contrib import admin
from .models import Feedback_new
from .models import Subject, Author
# Register your models here.

@admin.register(Feedback_new)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display =('name_m', 'text_m', 'is_active', 'created_at')
    list_editable =('is_active',)

@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display =('name_subject', 'name_bot', 'description', 'is_active', 'author')
    list_editable =('is_active','author',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('name',)
    
