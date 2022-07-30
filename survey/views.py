from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from survey.forms import PollForm, OptionsForm
from survey.models import Poll, ListChoice


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
        context['options'] = self.object.polls.all().order_by('-created_at')
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


class OptionAdd(CreateView):
    form_class = OptionsForm
    template_name = "options/option_add.html"

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class OptionUpdate(UpdateView):
    form_class = OptionsForm
    template_name = "options/option_update.html"
    model = ListChoice

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class OptionDelete(DeleteView):
    model = ListChoice
    template_name = "options/option_delete.html"

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})
