from typing import List

from fastapi import APIRouter

from app.internal import default_translator
from app.schema import TranslateIn, TranslateOut

router = APIRouter()


@router.post("/", response_model=List[TranslateOut])
async def translate(data: TranslateIn):
    """"""
    return default_translator.translate(
        input_text=data.input_text,
        source_lang=data.source_language,
        target_lang=data.destination_language,
    )
