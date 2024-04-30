from django.contrib import admin
from .models import BugReport, FeatureRequest

def set_status_new(modeladmin, request, queryset):
    queryset.update(status='New')
set_status_new.short_description = "Mark selected reports as New"
class BugReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'created_at', 'updated_at']
    list_filter = ['status', 'priority']
    search_fields = ['title', 'description']
    actions = [set_status_new]  # Добавление пользовательского действия

    # Настройка формы редактировния
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Advanced options', {
            'fields': ('status', 'priority', 'project', 'task'),
            'classes': ('collapse',)
        }),
    )

class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'created_at', 'updated_at']
    list_filter = ['status', 'priority']
    search_fields = ['title', 'description']

    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Advanced options', {
            'fields': ('status', 'priority', 'project', 'task'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(BugReport, BugReportAdmin)
admin.site.register(FeatureRequest, FeatureRequestAdmin)
