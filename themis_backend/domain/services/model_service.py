from abc import ABC, abstractmethod
from typing import Generator


class ModelService(ABC):
    @abstractmethod
    def generate(self, question: str) -> Generator[str, None, None]:
        ...

    @abstractmethod
    def tokenize(self, question: str) -> list[str]:
        ...
