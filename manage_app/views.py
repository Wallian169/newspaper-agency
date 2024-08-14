from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manage_app.models import Redactor, Newspaper, Topic


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
