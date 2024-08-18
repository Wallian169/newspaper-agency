from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manage_app.forms import (
    RedactorForm,
    RedactorUpdateForm,
    NewspaperForm,
    TopicSearchForm,
    RedactorSearchForm,
    NewspaperSearchForm,
)
from manage_app.models import Redactor, Newspaper, Topic


@login_required
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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = TopicSearchForm(self.request.GET)
        queryset = Topic.objects.all()
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("manage_app:topics")
    template_name = "manage_app/create_update_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("manage_app:topics")
    template_name = "manage_app/create_update_form.html"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("manage_app:topics")
    template_name = "manage_app/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "topic"
        context["object"] = self.object
        return context


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get("query`", "")
        context["search_form"] = RedactorSearchForm(
            initial={"query": search_input}
        )
        return context

    def get_queryset(self):
        form = RedactorSearchForm(self.request.GET)
        queryset = super().get_queryset()

        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(
                    Q(username__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query)
                )

        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newspapers = Newspaper.objects.filter(publishers__id=self.kwargs["pk"])
        context["newspapers"] = newspapers
        return context


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorForm
    template_name = "manage_app/create_update_form.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    template_name = "manage_app/create_update_form.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("manage_app:redactors")
    template_name = "manage_app/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "redactor"
        context["object"] = self.object.username
        return context


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        start_date = self.request.GET.get("start_date", "")
        end_date = self.request.GET.get("end_date", "")
        context["search_form"] = NewspaperSearchForm(
            initial={
                "title": title,
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)
        queryset = super().get_queryset()

        if form.is_valid():
            title = form.cleaned_data.get('title')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            if title:
                queryset = queryset.filter(title__icontains=title)

            if start_date and end_date:
                queryset = queryset.filter(
                    published_date__range=[start_date, end_date])
            elif start_date:
                queryset = queryset.filter(published_date__gte=start_date)
            elif end_date:
                queryset = queryset.filter(published_date__lte=end_date)

        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related("publishers")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "manage_app/create_update_form.html"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "manage_app/create_update_form.html"


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("manage_app:newspapers")
    template_name = "manage_app/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "newspaper"
        context["object"] = self.object.title
        return context
