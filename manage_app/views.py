from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manage_app.models import Redactor, Newspaper, Topic
from manage_app.forms import RedactorForm, RedactorUpdateForm


def index(request: HttpRequest) -> HttpResponse:
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
    }
    return render(
        request,
        "manage_app/index.html",
        context=context,
    )


class TopicListView(generic.ListView):
    model = Topic


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("manage_app:topics")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("manage_app:topics")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("manage_app:topics")
    template_name = "manage_app/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "topic"
        context["object"] = self.object
        return context


class RedactorListView(generic.ListView):
    model = Redactor


class RedactorDetailView(generic.DetailView):
    model = Redactor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newspapers = Newspaper.objects.filter(publishers__id=self.kwargs["pk"])
        context["newspapers"] = newspapers
        return context


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorForm


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("manage_app:redactors")
    template_name = "manage_app/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "redactor"
        context["object"] = self.object.username
        return context


class NewspaperListView(generic.ListView):
    model = Newspaper


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related("publishers")
