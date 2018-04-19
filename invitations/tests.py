from django.test import TestCase
from invitations.models import AppUser, Event, Rsvp
# Create your tests here.

class AppUserTestCase(TestCase):
    def setUp(self):
        AppUser.objects.create(
            first_name="Test",
            last_name="User",
            birth_date="10/25/2006",
            username="username",
            password1="password")
        AppUser.objects.create(
            first_name="Test1",
            last_name="User1",
            birth_date="1/25/2005",
            username="username1",
            password1="password")

    def users_have_first_name(self):
        test = AppUser.objects.get(username="username")
        test1 = AppUser.objects.get(username="username1")
        self.assertEqual(test.first_name(), "Test")
        self.assertEqual(test1.first_name(), "Test1")

    def users_have_last_name(self):
        test = AppUser.objects.get(username="username")
        test1 = AppUser.objects.get(username="username1")
        self.assertEqual(test.last_name(), "User")
        self.assertEqual(test1.last_name(), "User1")

    def users_have_birthdays(self):
        test = AppUser.objects.get(username="username")
        test1 = AppUser.objects.get(username="username1")
        self.assertEqual(test.birth_date(), "10/25/2006")
        self.assertEqual(test1.birth_date(), "1/25/2005")

# class EventTestCase(TestCase):
#     def setUp(self):
#         Event.objects.create(
#             title="Test's Party",
#             description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#             address="123 Address St.",
#             start_time="2006-10-25 14:30:59",
#             end_time="2006-10-26 14:30:59"
#         )
#         Event.objects.create(
#             title="Test 1's Party",
#             description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#             address="321 Address St.",
#             start_time="2006-10-25 14:30:59",
#             end_time="2006-10-26 14:30:59"
#         )
#
# class RsvpTestCase(TestCase):
#     def setUp(self):
#         pass
