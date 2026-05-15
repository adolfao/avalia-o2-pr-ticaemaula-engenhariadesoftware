class MaterialRepository:

    def __init__(self):
        self.materials = []

    def add_material(self, content):
        self.materials.append(content)

    def get_materials(self):
        return self.materials