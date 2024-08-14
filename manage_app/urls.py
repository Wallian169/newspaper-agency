from django.urls import path

from manage_app.views import index


urlpatterns = [
    path("", index, name="index"),
]

app_name = "manage_app"
