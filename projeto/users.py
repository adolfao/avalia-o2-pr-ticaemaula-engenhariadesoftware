class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    pass


class Student(User):
    pass


class Manager(User):
    pass


class UserFactory:
    @staticmethod
    def create_user(user_type, name):

        if user_type == "teacher":
            return Teacher(name)

        elif user_type == "student":
            return Student(name)

        elif user_type == "manager":
            return Manager(name)

        else:
            raise ValueError("Tipo inválido")