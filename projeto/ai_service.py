from abc import ABC, abstractmethod


class ResponseStrategy(ABC):

    @abstractmethod
    def respond(self, question, materials):
        pass


class NormalResponse(ResponseStrategy):

    def respond(self, question, materials):
        return f"Resposta normal baseada em: {materials}"


class SimplifiedResponse(ResponseStrategy):

    def respond(self, question, materials):
        return f"Resposta simplificada para neurodivergentes: {materials}"


class AIService:

    def __init__(self, strategy):
        self.strategy = strategy

    def answer_question(self, question, materials):
        return self.strategy.respond(question, materials)
    