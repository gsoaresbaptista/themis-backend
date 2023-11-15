import asyncio

from ctransformers import AutoModelForCausalLM

from themis_backend.config import ModelSettings
from themis_backend.domain.services import AsyncGenerator, BufferedGenerator


class GGUFModelService:
    def __init__(self) -> None:
        self.__model = AutoModelForCausalLM.from_pretrained(
            ModelSettings.FOLDER_PATH,
            model_file=ModelSettings.FILE_PATH,
            model_type=ModelSettings.TYPE,
            gpu_layers=ModelSettings.GPU_LAYERS,
        )
        self.__token_to_str = self.__model.ctransformers_llm_detokenize

    def generate(
        self, question: str, lock: asyncio.Lock = None
    ) -> BufferedGenerator:
        return BufferedGenerator(
            AsyncGenerator(self.__model(question, stream=True), lock)
        )

    def tokenize(self, question: str) -> list[str]:
        tokens = []
        for token in self.__model.tokenize(question):
            tokens.append(self.__token_to_str(token).decode('utf-8'))
        return tokens
