from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome,preco):
        self._preco = preco
        self._nome = nome

    @abstractmethod
    def desconto(self):
        pass