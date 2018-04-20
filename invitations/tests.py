from django.test import TestCase, Client
from invitations.models import AppUser, Event, Rsvp
from django.utils import timezone

# HTTP Tests
c = Client()
# Model Tests

class AppUserTestCase(TestCase):
    def setUp(self):
        AppUser.objects.create(
            first_name="Test",
            last_name="User",
            birth_date="2006-10-25",
            username="username",
            password="password")
        AppUser.objects.create(
            first_name="Test1",
            last_name="User1",
            birth_date="2005-1-25",
            username="username1",
            password="password")

    def test_users_have_attributes(self):
        test = AppUser.objects.get(username="username")
        test1 = AppUser.objects.get(username="username1")

        self.assertEqual(test.first_name, "Test")
        self.assertEqual(test1.first_name, "Test1")
        self.assertEqual(test.last_name, "User")
        self.assertEqual(test1.last_name, "User1")
        self.assertEqual(str(test.birth_date), '2006-10-25')
        self.assertEqual(str(test1.birth_date), '2005-01-25')

class EventTestCase(TestCase):
    def setUp(self):
        AppUser.objects.create(
            first_name="Test",
            last_name="User",
            birth_date="2006-10-25",
            username="username",
            password="password")
        AppUser.objects.create(
            first_name="Test1",
            last_name="User1",
            birth_date="2005-1-25",
            username="username1",
            password="password")
        Event.objects.create(
            creator=AppUser.objects.get(username="username"),
            title="Test's Party",
            description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
            address="123 Address St.",
            start_time="2006-10-25 14:30:59.920830+00:00",
            end_time="2006-10-26 14:30:59.920830+00:00"
        )
        Event.objects.create(
            creator=AppUser.objects.get(username="username1"),
            title="Test 1's Party",
            description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
            address="321 Address St.",
            start_time="2006-10-25 14:30:59.920830+00:00",
            end_time="2006-10-26 14:30:59.920830+00:00"
        )

    def test_events_have_attributes(self):
        test = AppUser.objects.get(username="username")
        test1 = AppUser.objects.get(username="username1")
        test_party = Event.objects.get(title="Test's Party")
        test1_party = Event.objects.get(title="Test 1's Party")

        self.assertEqual(test_party.creator, test)
        self.assertEqual(test1_party.creator, test1)
        self.assertEqual(test_party.title, "Test's Party")
        self.assertEqual(test1_party.title, "Test 1's Party")
        self.assertEqual(test_party.address, "123 Address St.")
        self.assertEqual(test1_party.address, "321 Address St.")
        self.assertIn("Lorem ipsum dolor sit amet", test_party.description)
        self.assertIn("Lorem ipsum dolor sit amet", test1_party.description)
        self.assertEqual(str(test_party.start_time), "2006-10-25 14:30:59.920830+00:00")
        self.assertEqual(str(test1_party.start_time), "2006-10-25 14:30:59.920830+00:00")
        self.assertEqual(str(test_party.end_time), "2006-10-26 14:30:59.920830+00:00")
        self.assertEqual(str(test1_party.end_time), "2006-10-26 14:30:59.920830+00:00")

class RsvpTestCase(TestCase):
    def test_invitation_properties(self):
        test = AppUser.objects.create(
                    first_name="Test",
                    last_name="User",
                    birth_date="2006-10-25",
                    username="username",
                    password="password"
                )
        test1 = AppUser.objects.create(
                    first_name="Test1",
                    last_name="User1",
                    birth_date="2005-1-25",
                    username="username1",
                    password="password"
                )
        event = Event.objects.create(
                    creator=AppUser.objects.get(username="username"),
                    title="Test's Party",
                    description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
                    address="123 Address St.",
                    start_time="2006-10-25 14:30:59.920830+00:00",
                    end_time="2006-10-26 14:30:59.920830+00:00"
                )

        rsvp = Rsvp.objects.create(
            event=event,
            invitee=test1,
            is_attending=True
        )

        self.assertEqual(rsvp.event, event)
        self.assertEqual(rsvp.invitee, test1)
        self.assertTrue(rsvp.is_attending)
        self.assertIn(test1, event.invitees.all())
