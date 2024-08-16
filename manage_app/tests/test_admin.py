from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_admin = get_user_model().objects.create_superuser(
            username="admin",
            password="test_admin",
        )
        self.client.force_login(self.user_admin)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            first_name="first",
            last_name="last",
        )

    def test_years_of_experience_field(self):
        """
            Testing if the years of experience field
            is presented at admin page
            :return:
        """
        url = reverse("admin:manage_app_redactor_changelist")
        response = self.client.get(url)
        self.assertContains(
            response, self.redactor.years_of_experience
        )

    def test_redactor_detail_years_field(self):
        """
            Testing if the years of experience field
            is presented at redactor detail page
            :return:
        """
        url = reverse(
            "admin:manage_app_redactor_change",
            args=[self.redactor.id]
        )
        response = self.client.get(url)
        self.assertContains(response, self.redactor.years_of_experience)

    def test_addition_info_fieldset(self):
        """
            Testing if the addition info fieldset
            is presented at redactor detail page
            :return:
        """
        url = reverse(
            "admin:manage_app_redactor_change",
            args=[self.redactor.id]
        )
        response = self.client.get(url)
        self.assertContains(
            response,
            self.redactor.years_of_experience
        )
