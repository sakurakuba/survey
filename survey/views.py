from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from survey.forms import PollForm
from survey.models import Poll


class Index(ListView):
    model = Poll
    template_name = "index.html"
    context_object_name = "polls"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_queryset(self):
        return Poll.objects.order_by("-created_at")


class PollView(DetailView):
    template_name = 'poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super(PollView, self).get_context_data(**kwargs)
        #context['polls'] = self.object.polls.all().order_by('-created_at')
        return context


class PollCreate(CreateView):
    form_class = PollForm
    template_name = "poll_create.html"


class PollUpdate(UpdateView):
        template_name = 'poll_update.html'
        form_class = PollForm
        model = Poll


class PollDelete(DeleteView):
    model = Poll
    template_name = "poll_delete.html"
    success_url = reverse_lazy("index")
