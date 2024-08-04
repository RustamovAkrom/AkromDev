from django.test import TestCase
from django.urls import reverse
from apps.users.models import User, UserAccount


class UserTestCase(TestCase):
    def setUp(self) -> None:
        # user = User.objects.create(
        #     first_name="Akrom",
        #     last_name="Rustamov",
        #     username = "Akromjon",
        #     email="akromjonrustamov56@gmail.com"
        # )
        # user.set_password("2007")
        # user.save()
        # user_account = UserAccount.objects.create(

        # )
        return super().setUp()
    
    def test_user_auth(self):
        pages = ["users:sign-in", "users:sign-up"]

        for page in pages:
            url = "http://127.0.0.1" + reverse(page)
            response = self.client.get(path=url)
            self.assertEqual(response.status_code, 200)