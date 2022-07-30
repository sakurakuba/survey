from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.datetime_safe import date


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    class Meta:
        abstract = True


class Poll(BaseModel):
    poll_question = models.CharField(max_length=100, verbose_name='Poll question')

    def __str__(self):
        return f"{self.poll_question}"

    def get_absolute_url(self):
        return reverse('poll_view', kwargs={"pk": self.pk})

    class Meta:
        db_table = 'polls'
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'


class ListChoice(BaseModel):
    choice_text = models.CharField(max_length=100, verbose_name='Choice text')
    poll = models.ForeignKey("survey.Poll", on_delete=models.CASCADE, related_name='polls', verbose_name='Poll')

    def __str__(self):
        return f"{self.choice_text} - poll: {self.poll}"

    class Meta:
        db_table = 'listChoices'
        verbose_name = 'LictChoice'
        verbose_name_plural = 'LictChoices'



