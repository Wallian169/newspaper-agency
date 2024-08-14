from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
