from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
	"""Unit Testing The User with email """
	def test_user_model_with_email_completely(self):
		email="test123@gmail.com"
		password="django12345"
		user=get_user_model().objects.create_user(
			email=email,
			password=password

		)
		self.assertEqual(user.email,email)
		self.assertTrue(user.check_password(password))


	def test_user_mail_normalize_properly(self):
		"""This test the New mail  normalize properly"""
		email="test123@gmail.com"
		user=get_user_model().objects.create_user(email,"test123")

		self.assertEqual(user.email,email.lower())

	

	def test_email_with_invalid_input(self):
		"""This test test the user put the email on emailField or not"""

		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None,"test123")

	def test_create_user_with_super_user(self):
	    """Test creating a user with superuser status"""

	    # Using create_superuser instead of create_user
	    user = get_user_model().objects.create_superuser(
	        email="test123@gmail.com",
	        password="test123"
	    )

	    # Assertions
	    self.assertTrue(user.is_superuser)
	    self.assertTrue(user.is_staff)
	    self.assertTrue(user.is_active)
	    self.assertEqual(user.email, "test123@gmail.com")
