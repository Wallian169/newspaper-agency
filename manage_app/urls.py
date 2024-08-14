from django.urls import path

from manage_app.views import (
    index,
    TopicListView,
    TopicCreateView,

)


urlpatterns = [
    path("", index, name="index"),
    path("/topics/", TopicListView.as_view(), name="topics"),
    path("/topics/create/", TopicCreateView.as_view(), name="topic-create"),
]

app_name = "manage_app"
