from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
	fieldsets = (
        (None, {
            'fields': ('name', 'path', 'html',)
        }),
    )
	class Meta:
		model = Page

admin.site.register(Page, PageAdmin)
