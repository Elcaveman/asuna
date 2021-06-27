from django import forms
from .models import *

class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewModel
        fields = '__all__'

class InterviewMetadataForm(forms.ModelForm):
    class Meta:
        model = InterviewMetadataModel
        fields = '__all__'

class ChatHistoryForm(forms.ModelForm):
    class Meta:
        model = ChatHistory
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
