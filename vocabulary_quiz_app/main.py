from error_notebook import save_error_word, show_all_error
from __future__ import annotations

import tkinter as tk

from vocabulary_quiz_app.app import VocabularyQuizApp
from vocabulary_quiz_app.data import WORDS


def main() -> int:
    root = tk.Tk()
    VocabularyQuizApp(root, WORDS)
    root.mainloop()
    return 0


if __name__ == "__main__":
    main()
