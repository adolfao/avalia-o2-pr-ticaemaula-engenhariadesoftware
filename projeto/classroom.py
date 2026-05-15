class Classroom:

    def __init__(self, name, repository):
        self.name = name
        self.repository = repository

    def upload_material(self, material):
        self.repository.add_material(material)