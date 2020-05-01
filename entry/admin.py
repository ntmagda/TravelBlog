from django.contrib import admin
from django.contrib import admin

from .models import Entry, EntryImage, EntryVideo, EntryTipFullArticle, EntrySmallTip, Country

class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['name']



class EntryImageInline(admin.TabularInline):
    model = EntryImage
    extra = 3


class EntryVideoInline(admin.TabularInline):
    model = EntryVideo
    extra = 1

class EntryTipInline(admin.TabularInline):
    model = EntrySmallTip
    extra = 3


class EntryAdmin(admin.ModelAdmin):
    inlines = [EntryImageInline, EntryVideoInline, EntryTipInline, ]
    list_display = ['title', 'short_body','slug','get_tags']

    def get_tags(self, entry):
        tags = []
        for tag in entry.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


class EntryTipFullArticleAdmin(admin.ModelAdmin):
    model = EntryTipFullArticle
    list_display = ['title', 'short_body', 'slug', 'get_tags']

    def get_tags(self, entry):
        tags = []
        for tag in entry.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


admin.site.register(EntryTipFullArticle, EntryTipFullArticleAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Country, CountryAdmin)