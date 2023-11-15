from abc import ABC, abstractmethod
from typing import Generator


class BufferedGenerator:
    def __init__(self, default_generator: Generator[str, None, None]):
        self.__generator = default_generator
        self.__buffer = ''

    def send(self, value=None) -> str:
        text = next(self.__generator)
        self.__buffer += text
        return text

    def __next__(self):
        return self.send(None)

    def __iter__(self):
        return self

    def get_text(self) -> str:
        return self.__buffer


class ModelService(ABC):
    @abstractmethod
    def generate(self, question: str) -> BufferedGenerator:
        ...

    @abstractmethod
    def tokenize(self, question: str) -> list[str]:
        ...
