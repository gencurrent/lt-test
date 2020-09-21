import logging

from django.conf import settings
from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe, escape

from .models import Branch, Employee

logger = logging.getLogger()

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'facade_image', 'latitude', 'longitude',)
    search_fields = ('name', 'latitude', 'longitude')

    fieldsets = (
        (None, {
            'fields': ( 'name', 'facade_image', 'latitude', 'longitude',)
        }),
    )

    # def get_fieldsets(self, request, obj=None):
    #     logger.info(f'Here')
    #     if request.user.is_superuser:
    #         logger.info(f'It is admin')
    #         return BranchAdmin.fieldsets
    #     else: 
    #         return (
    #             (None, {
    #                 'fields': ( 'name', 'facade_image',)
    #             }),
    #         )
    #     return super().get_fieldsets(request, obj)
        

    class Media:
        css = {
            'all': ('css/admin/location_picker.css',),
        }
        js = (
            'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
            'js/admin/location_picker.js',
        )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'third_name', 'position_title', 'get_branch_name')
    search_fields = ('first_name', 'third_name', 'position_title',)

    def get_branch_name(self, obj:Employee):
        if obj.branch:
            link = reverse("admin:organization_branch_change", args=[obj.branch_id])
            return mark_safe(f'<a href="{link}">{escape(obj.branch.__str__())}</a>')
        return '-'*4


    
    get_branch_name.short_description = 'Branch'