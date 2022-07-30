from django import forms
from django.forms import widgets
from django.forms import ModelMultipleChoiceField

from .models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["poll_question"]


# class PollForm(forms.ModelForm):
#     class Meta:
#         model = Poll
#         fields = ["poll_question"]
#         widgets = {
#             "type": widgets.CheckboxSelectMultiple,
#             "description": widgets.Textarea(attrs={"placeholder": "please add text here"})
#         }




