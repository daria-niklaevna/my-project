from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Car, Manufacturer, Driver


class ModelTests(TestCase):

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="X-test",
            country="Test"
        )
        car = Car.objects.create(
            model="test",
            manufacturer=manufacturer,
        )

        self.assertEqual(str(car), car.model)

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="Test first",
            last_name="Test last"
        )

        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="X-test",
            country="Test"
        )

        self.assertEqual(str(manufacturer), f"{manufacturer.name} ({manufacturer.country})")

    def test_create_driver_with_license_number(self):
        username = "test"
        password = "test1234"
        license_number = "SDF45962"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)

    def test_get_absolute_url(self):
        driver = get_user_model().objects.create_user(
            id=1,
            username="test",
            password="test1234",
            first_name="Test first",
            last_name="Test last"
        )
        driver_test = Driver.objects.get(id=1)

        self.assertEquals(driver_test.get_absolute_url(), '/drivers/1/')
