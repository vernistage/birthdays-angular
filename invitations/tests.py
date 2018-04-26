from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from invitations.models import AppUser, Event, Rsvp
from django.utils import timezone

# HTTP Tests
class HTTPLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logged_out_welcome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in")
        self.assertContains(response, "Register")

    def test_logged_out_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")
        self.assertContains(response, "Sign up")

    def test_logged_out_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_profile(self):
        response = self.client.get('/user/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_events(self):
        response = self.client.get(reverse('invitations:events'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_event_detail_page(self):
        response = self.client.get('/events/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_event_create_page(self):
        response = self.client.get(reverse('invitations:create_event'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_event_create_page(self):
        response = self.client.get('/events/edit/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_event_destroy(self):
        response = self.client.get('/events/destroy/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_rsvps(self):
        response = self.client.get(reverse('invitations:rsvps'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

    def test_logged_out_rsvp_edit(self):
        response = self.client.get('/rsvps/edit/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")

class HTTPLoggedIn(TestCase):
    def setUp(self):
        self.invitee = AppUser.objects.create(username='invitee',
                                            password='password',
                                            first_name='iam',
                                            last_name='invited',
                                            birth_date='1987-01-01')
        self.user = AppUser.objects.create(username='testuser',
                                            first_name='test',
                                            last_name='user',
                                            birth_date='1987-01-01')
        self.client = Client()
        self.client.force_login(self.user, backend=None)
        self.event = Event.objects.create(
            creator=self.user,
            title="Test's Party",
            description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
            address="123 Address St.",
            start_time="2006-10-25 14:30:59.920830+00:00",
            end_time="2006-10-26 14:30:59.920830+00:00"
        )
        self.rsvp = Rsvp.objects.create(
            event=self.event,
            invitee=self.invitee,
            is_attending=True,
        )

    def test_logged_in_welcome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profile")
        self.assertContains(response, "Log out")

    def test_logged_in_profile(self):
        response = self.client.get(reverse('user_profile',
                                            kwargs={'pk': self.user.pk}),
                                            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertContains(response, "Hello")



    def test_logged_in_events(self):
        response = self.client.get(reverse('invitations:events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manage Events")

    def test_logged_in_event(self):
        response = self.client.get(reverse('invitations:event',
                                            kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "created by")

    def test_logged_in_event_create_page(self):
        response = self.client.get(reverse('invitations:create_event'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Event" or "Edit")

    def test_logged_in_event_edit_page(self):
        response = self.client.get(reverse('invitations:update_event',
                                            kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit")

    def test_logged_in_event_destroy_page(self):
        response = self.client.get(reverse('invitations:destroy_event',
                                            kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_rsvps(self):
        response = self.client.get(reverse('invitations:rsvps'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invitations to you")

    def test_logged_in_rsvp_edit(self):
        response = self.client.get(reverse('invitations:update_rsvp',
                                            kwargs={'pk': self.rsvp.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "RSVP for")

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
