from django import forms
from .models import Poll, ListChoice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["poll_question"]


class OptionsForm(forms.ModelForm):
    class Meta:
        model = ListChoice
        fields = ["choice_text"]



