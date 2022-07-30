from django.contrib import admin

# Register your models here.
from survey.models import Poll, ListChoice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll_question', 'created_at']
    list_display_links = ['poll_question']
    list_filter = ['poll_question']
    search_fields = ['poll_question']
    fields = ['poll_question', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class ListChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'choice_text']
    list_display_links = ['poll']
    list_filter = ['poll']
    search_fields = ['poll', 'choice_text']
    fields = ['poll', 'choice_text']


admin.site.register(Poll, PollAdmin)
admin.site.register(ListChoice, ListChoiceAdmin)
