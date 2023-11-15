from ctransformers import AutoModelForCausalLM
from starlette.applications import Starlette

from themis_backend.config import ModelSettings
from themis_backend.infra.database import create_tables


async def startup_event_handler() -> None:
    await create_tables()


def setup_startup(app: Starlette) -> None:
    app.add_event_handler('startup', startup_event_handler)
    app.model = AutoModelForCausalLM.from_pretrained(
        ModelSettings.FOLDER_PATH,
        model_file=ModelSettings.FILE_PATH,
        model_type=ModelSettings.TYPE,
        gpu_layers=ModelSettings.GPU_LAYERS,
    )
