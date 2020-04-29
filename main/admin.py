from django.contrib import admin
from django.contrib import admin

from .models import AboutUsImage, AboutUs

class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 3
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInline, ]
    list_display = ['title','leon_image','magda_image']

admin.site.register(AboutUs, AboutUsAdmin)
