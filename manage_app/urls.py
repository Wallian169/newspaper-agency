from django.urls import path

from manage_app.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView, RedactorListView,
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
]

app_name = "manage_app"
