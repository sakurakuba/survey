from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.datetime_safe import date


class Poll(models.Model):
    poll_question = models.CharField(max_length=100, verbose_name='Poll question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __str__(self):
        return f"{self.poll_question}"

    class Meta:
        db_table = 'polls'
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'


class ListChoice(models.Model):
    choice_text = models.CharField(max_length=100, verbose_name='Choice text')
    poll = models.ForeignKey("survey.Poll", on_delete=models.CASCADE, related_name='polls', verbose_name='Poll')

    def __str__(self):
        return f"{self.choice_text} - poll: {self.poll}"

    class Meta:
        db_table = 'listChoices'
        verbose_name = 'LictChoice'
        verbose_name_plural = 'LictChoices'



