from enum import Enum

from pydantic import BaseModel


class LangChoices(str, Enum):
    English = "en"
    French = "fr"
    German = "de"
    Romanian = "ro"


class TranslateIn(BaseModel):
    source_language: LangChoices
    destination_language: LangChoices
    input_text: str


class TranslateOut(BaseModel):
    translation_text: str
