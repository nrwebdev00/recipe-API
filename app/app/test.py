from django.test import SimpleTestCase

from app import clac


class ClacTests(SimpleTestCase):

    def test_add_numbers(self):
        res = clac.add(15, 20)

        self.assertEqual(res, 35)

    def test_subtract_number(self):
        res = clac.sub(15, 20)

        self.assertEqual(res, -5)
        