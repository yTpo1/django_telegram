from django.contrib import admin
from .models import Channel, Category, Language


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'language',)
    # search_fields = ('title',)
    list_filter = ('category', 'language',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)

