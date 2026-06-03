from error_notebook import save_error_word, show_all_error
from __future__ import annotations

import random

from dataclasses import dataclass


@dataclass(frozen=True)
class Word:
    term: str
    meaning: str


def normalize_answer(text: str) -> str:
    return " ".join(text.strip().lower().split())


def check_answer(word: Word, user_input: str) -> bool:
    res = normalize_answer(user_input) == normalize_answer(word.meaning)
    if not res:
        # 答错了，存入错题本
        save_error_word(word.term, word.meaning)
    return res

def draw_word(words: list[Word], rng: random.Random | None = None) -> Word:
    if not words:
        raise ValueError("Word list is empty")
    chooser = rng if rng is not None else random
    return chooser.choice(words)
