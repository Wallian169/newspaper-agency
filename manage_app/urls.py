from django.urls import path

from manage_app.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    NewspaperListView, NewspaperDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topics"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/update/<int:pk>/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/delete/<int:pk>/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path("redactors/", RedactorListView.as_view(), name="redactors"),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/update/<int:pk>/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/delete/<int:pk>/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspapers"
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    )
]

app_name = "manage_app"
