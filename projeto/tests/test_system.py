import unittest

from users import UserFactory, Teacher
from materials import MaterialRepository


class TestUserFactory(unittest.TestCase):

    # Cenário de sucesso
    def test_create_teacher_success(self):

        user = UserFactory.create_user("teacher", "Carlos")

        self.assertIsInstance(user, Teacher)
        self.assertEqual(user.name, "Carlos")

    # Cenário de falha/exceção
    def test_create_invalid_user(self):

        with self.assertRaises(ValueError):
            UserFactory.create_user("invalid", "Teste")

    # Cenário de borda
    def test_create_user_empty_name(self):

        user = UserFactory.create_user("teacher", "")

        self.assertEqual(user.name, "")


class TestMaterialRepository(unittest.TestCase):

    # Cenário de sucesso
    def test_add_material_success(self):

        repo = MaterialRepository()

        repo.add_material("Fotossíntese")

        self.assertIn("Fotossíntese", repo.get_materials())

    # Cenário de falha
    def test_add_none_material(self):

        repo = MaterialRepository()

        repo.add_material(None)

        self.assertIn(None, repo.get_materials())

    # Cenário de borda
    def test_add_empty_material(self):

        repo = MaterialRepository()

        repo.add_material("")

        self.assertIn("", repo.get_materials())


if __name__ == "__main__":
    unittest.main()