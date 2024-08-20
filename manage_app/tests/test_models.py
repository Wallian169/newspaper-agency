import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manage_app.models import Topic, Newspaper


class ModelTest(TestCase):

    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")

        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            first_name="first",
            last_name="last",
        )

        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="This is a test newspaper content.",
            published_date=datetime.date(2024, 8, 16)
        )
        self.newspaper.publishers.add(self.redactor)
        self.newspaper.topics.add(self.topic)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Test Topic")

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), "first last")

    def test_redactor_absolute_url(self):
        expected_url = reverse(
            "manage_app:redactor-detail", kwargs={"pk": self.redactor.pk})
        self.assertEqual(self.redactor.get_absolute_url(), expected_url)

    def test_newspaper_creation(self):
        self.assertEqual(self.newspaper.title, "Test Newspaper")
        self.assertEqual(
            self.newspaper.content, "This is a test newspaper content.")
        self.assertEqual(
            self.newspaper.published_date, datetime.date(2024, 8, 16))

    def test_publishers_relationship(self):
        self.assertIn(self.redactor, self.newspaper.publishers.all())

    def test_topics_relationship(self):
        self.assertIn(self.topic, self.newspaper.topics.all())

    def test_get_absolute_url(self):
        self.assertEqual(
            self.newspaper.get_absolute_url(),
            f"/newspapers/{self.newspaper.pk}/"
        )
