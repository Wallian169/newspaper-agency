from django.urls import path

from manage_app.views import (
    index,
    TopicListView
)


urlpatterns = [
    path("", index, name="index"),
    path("/topics/", TopicListView.as_view(), name="topics"),
]

app_name = "manage_app"
