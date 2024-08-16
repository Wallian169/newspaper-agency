from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from manage_app.models import Redactor, Newspaper, Topic


class RedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self):
        return validate_years_number(
            self.cleaned_data["years_of_experience"]
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["username", "first_name", "last_name", "years_of_experience"]

    def clean_years_of_experience(self):
        return validate_years_number(self.cleaned_data["years_of_experience"])


def validate_years_number(years_of_experience: int) -> int:
    years_limit = 50
    if years_of_experience > years_limit:
        raise ValidationError(
            f"Years field must be less than or equal to {years_limit}"
        )

    return years_of_experience


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    published_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        )
    )


class RedactorSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username, first name, or last name"}
        )
    )
