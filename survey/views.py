from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from survey.models import Poll


class Index(ListView):
    model = Poll
    template_name = "index.html"
    context_object_name = "polls"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_queryset(self):
        return Poll.objects.order_by("-created_at")

