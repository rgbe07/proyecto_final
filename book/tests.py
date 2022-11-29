import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from book.models import Book


class BookTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Book.objects.create(name="Python", isbn=123, owner=self.test_user)
        Book.objects.create(name="Docker", isbn=789, owner=self.test_user)

        book_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(book_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(book_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Book.objects.create(name=mock_name, isbn=mock_code, owner=self.test_user)

    def test_book_model(self):
        """Books creation are correctly identified"""
        python_book = Book.objects.get(name="Python")
        docker_book = Book.objects.get(name="Docker")
        self.assertEqual(python_book.owner.username, "testuser")
        self.assertEqual(docker_book.owner.username, "testuser")
        self.assertEqual(python_book.isbn, 123)
        self.assertEqual(docker_book.isbn, 789)

    def test_book_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            book_test = Book.objects.get(name=mock_name)
            self.assertEqual(book_test.owner.username, "testuser")
            self.assertEqual(book_test.isbn, mock_code)
