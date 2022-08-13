from typing import List, Optional

from loguru import logger
from transformers import (
    PreTrainedTokenizer,
    T5ForConditionalGeneration,
    T5Tokenizer,
    pipeline,
)

from app.core.config import settings
from app.schema.translate import LangChoices, TranslateOut


class Translator:
    def __init__(self):
        """
        translator class
        """
        self.model_name = "t5-base"
        self.tokenizer_name = "t5-base"

        self._is_init = False
        self.tokenizer: Optional[PreTrainedTokenizer] = None
        self.model: Optional[T5ForConditionalGeneration] = None

    def init_model(self):
        logger.debug("initializing model...")
        if not self._is_init:
            self.tokenizer = T5Tokenizer(
                vocab_file=f"{settings.MODEL_DIR}/spiece.model"
            ).from_pretrained(settings.MODEL_DIR, model_max_length=512)
            self.model = T5ForConditionalGeneration.from_pretrained(settings.MODEL_DIR)
            self._is_init = True

    def translate(
        self, input_text: str, *, source_lang: LangChoices, target_lang: LangChoices
    ) -> List[TranslateOut]:
        """
        translate input_text from source_lang to target_lang
        :param source_lang: language for input text
        :param target_lang: language to translate input text to
        :param input_text: the text to translate
        """

        if not self._is_init:
            raise ValueError(
                f"call init_model() on the '{self.__class__.__name__}' class first before calling .translate()"
            )

        task = f"translation_{source_lang.value}_to_{target_lang.value}"

        tr = pipeline(task, model=self.model, tokenizer=self.tokenizer, framework="pt")
        return tr(input_text)


default_translator = Translator()
