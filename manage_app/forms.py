from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from manage_app.models import Redactor


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


def validate_years_number(years_of_experience: int) -> int:
    years_limit = 50
    if years_of_experience > years_limit:
        raise ValidationError(
            f"Years field must be less than or equal to {years_limit}"
        )

    return years_of_experience
