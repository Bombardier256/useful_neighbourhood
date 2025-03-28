from unicodedata import category

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from lend_assist.models import (
    Category,
    Neighbour,
    Service,
    Request,
)


class ModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")
        self.neighbour = Neighbour.objects.create(
            username="test100",
            first_name="John",
            last_name="Smith",
            phone="+380501111111",
        )

    def test_category_model(self):
        obj = self.category
        self.assertEqual(str(obj), obj.name)

    def test_neighbour_model(self):
        obj = self.neighbour
        self.assertEqual(str(obj), obj.username)
        self.assertEqual(
            obj.phone, "+380501111111"
        )

    def test_service_model(self):
        obj = Service.objects.create(
            name="test",
            description="tests",
            free_of_charge=True,
            is_lending=True,
            category=self.category,
        )
        obj.neighbours.add(self.neighbour)
        obj.save()
        self.assertEqual(str(obj), obj.name)
        self.assertEqual(obj.category, self.category)

    def test_request_model(self):
        obj = Request.objects.create(
            name="test2",
            description="tests2",
            complete=False,
            category=self.category,
        )
        obj.neighbours.add(self.neighbour)
        obj.save()
        self.assertEqual(str(obj), obj.name)
        self.assertEqual(obj.category, self.category)

    def test_login_required(self):
        response = self.client.get(reverse("lend_assist:service-list"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("lend_assist:rental-list"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("lend_assist:request-list"))
        self.assertNotEqual(response.status_code, 200)


class LoggedInViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="test1",
            password="12345678"
        )
        self.client.force_login(self.user)
        self.category = Category.objects.create(name="test")
        self.service1 = Service.objects.create(
            name="Test22",
            description="tests",
            free_of_charge=True,
            is_lending=False,
            category=self.category,
        )
        self.service2 = Service.objects.create(
            name="Icecream",
            description="tests",
            free_of_charge=True,
            is_lending=False,
            category=self.category,
        )

    def test_retrieve_service_name(self):
        response = self.client.get(reverse("lend_assist:service-list"))
        self.assertEqual(response.status_code, 200)
        service_list = Service.objects.all()
        self.assertEqual(list(response.context["service_list"]), list(service_list))
        self.assertTemplateUsed(
            response, "lend_assist/service_list.html"
        )

    def test_search_service_name(self):
        response = self.client.get(
            reverse("lend_assist:service-list") + "?title=M"
        )
        service_with_m = Service.objects.filter(name__contains="M")
        self.assertEqual(list(response.context["service_list"]), list(service_with_m))

    def test_service_is_rental(self):
        Service.objects.create(
            name="Rent_tools",
            description="tests",
            free_of_charge=True,
            is_lending=True,
            category=self.category,
        )
        response = self.client.get(reverse("lend_assist:rental-list"))
        rental_list = Service.objects.filter(is_lending=True)
        self.assertEqual(list(response.context["rental_list"]), list(rental_list))
