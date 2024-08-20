from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from manage_app.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    TopicListCreateView,
    TopicUpdateDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListCreateView.as_view(), name="topics"),
    path(
        "topics/<int:pk>/",
        TopicUpdateDeleteView.as_view(),
        name="topic-update-delete"
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
    ),
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers/update/<int:pk>/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/delete/<int:pk>/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "manage_app"
