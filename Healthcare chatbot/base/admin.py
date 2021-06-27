from django.contrib import admin
from .models import *

class InterviewAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)
    list_display = ('user','interview_id',)

class MessageInline(admin.TabularInline):
    model = Message

class ChatHistoryAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline,
    ]

class PaternsInline(admin.TabularInline):
    model = Patern
class ResponsesInline(admin.TabularInline):
    model = Response
class SymptomAdmin(admin.ModelAdmin):
    inlines = [
        PaternsInline,
        ResponsesInline,
    ]

admin.site.register(InterviewModel,InterviewAdmin)
admin.site.register(InterviewMetadataModel)
admin.site.register(ChatHistory,ChatHistoryAdmin)
admin.site.register(Symptom,SymptomAdmin)
admin.site.register(Disease)
