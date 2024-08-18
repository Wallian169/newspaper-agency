from django.contrib.auth import get_user_model
from django.test import TestCase

from manage_app.forms import RedactorForm

User = get_user_model()


class RedactorFormTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

    def test_valid_form(self):
        form_data = {
            'username': 'newredactor',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'years_of_experience': 5,
            'first_name': 'John',
            'last_name': 'Doe'
        }
        form = RedactorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience(self):
        form_data = {
            'username': 'newredactor',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'years_of_experience': 51,  # Invalid value
            'first_name': 'John',
            'last_name': 'Doe'
        }
        form = RedactorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('years_of_experience', form.errors)
        self.assertEqual(
            form.errors['years_of_experience'],
            ['Years field must be less than or equal to 50']
        )
