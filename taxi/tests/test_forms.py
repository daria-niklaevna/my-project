from django.test import TestCase

from taxi.forms import DriverCreationForm, LicenseForm


class FormsTests(TestCase):
    def test_driver_creation_form(self):
        form_data = {
            "username": "new_user",
            "password1": "user1234",
            "password2": "user1234",
            "license_number": "SDF12589",
            "first_name": "Test first",
            "last_name": "Test last"
        }
        form = DriverCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_license_form(self):
        form_data = {
            "license_number": "SDF12589",
        }
        form = LicenseForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
