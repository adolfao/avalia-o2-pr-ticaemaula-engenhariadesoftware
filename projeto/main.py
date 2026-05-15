from users import UserFactory
from materials import MaterialRepository
from classroom import Classroom
from ai_service import AIService, NormalResponse, SimplifiedResponse

# Factory Method
teacher = UserFactory.create_user("teacher", "Carlos")
student = UserFactory.create_user("student", "Ana")

# Sala e materiais
repository = MaterialRepository()

classroom = Classroom("Ciências", repository)

classroom.upload_material(
    "Fotossíntese é o processo onde plantas produzem energia."
)

# Strategy Pattern
normal_ai = AIService(NormalResponse())

response = normal_ai.answer_question(
    "O que é fotossíntese?",
    repository.get_materials()
)

print(response)

simplified_ai = AIService(SimplifiedResponse())

response2 = simplified_ai.answer_question(
    "Explique fotossíntese",
    repository.get_materials()
)

print(response2)