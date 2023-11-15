import random
import string
import time
from typing import Generator

from themis_backend.domain.services import BufferedGenerator


class RandomModelService:
    def __init__(self) -> None:
        self.__model = random_generator

    def generate(self, question: str) -> BufferedGenerator:
        return BufferedGenerator(self.__model())

    def tokenize(self, question: str) -> list[str]:
        return question.split(' ')


def generate_random_word(length: int = 5) -> str:
    """generate a random word with the specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def random_generator() -> Generator[str, None, None]:
    length = random.randint(5, 100)
    for phrase in [
        generate_random_word(random.randint(5, 10)) for _ in range(length)
    ]:
        yield phrase + ' '
        time.sleep(random.uniform(0.001, 0.1))
